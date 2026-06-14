<?php
/**
 * Kudos Circle — short invite-link store/lookup endpoint.
 *
 * Built by Sprout, an autonomous AI agent (AI-authored — see chatforest.com/kudos).
 *
 * WHY: invite links carry the whole circle (name + every member address + a nonce).
 * Base64-JSON'd into a URL fragment that runs ~400 chars, which hurts shareability —
 * and shareable referral links are a judged criterion. This endpoint stores the
 * payload once and hands back a short, unguessable code so the link becomes
 *   https://chatforest.com/kudos/#i=<code>
 *
 * Deploy: this file lives in the kudos app's public/ dir, so Vite copies it verbatim
 * into the build (dist/api/invite.php) which the grove pipeline publishes to the Hugo
 * site at static/kudos/api/invite.php -> served same-origin as /kudos/api/invite.php.
 * No CORS needed (same origin as the static app).
 *
 * API:
 *   POST  (JSON body {circle, inviter, members[], code, exp})  -> 200 {"short_code": "..."}
 *   GET   ?c=<short_code>                                       -> 200 <payload JSON> | 404
 *
 * DB creds: read from a .my.cnf-style ini at an absolute path OUTSIDE the web root via
 * parse_ini_file(). Never hard-coded, never committed (a .example sits beside this file).
 */

declare(strict_types=1);

// ---- config -----------------------------------------------------------------

// Absolute path to the DB credentials ini (a .my.cnf [client] section). Kept OUTSIDE
// the web root; Boss places the real file (chmod 600) on DreamHost at deploy time.
if (!defined('KUDOS_DB_CNF')) {
    define('KUDOS_DB_CNF', '/home/backforest/.kudos_db.cnf');
}

const KUDOS_MAX_BODY_BYTES   = 8192;  // reject bodies larger than this (anti-abuse)
const KUDOS_MAX_PAYLOAD_JSON = 6144;  // reject stored payloads larger than this
const KUDOS_MAX_MEMBERS      = 50;    // a circle is a small team, not a crowd
const KUDOS_MAX_CIRCLE_LEN   = 200;   // sanitized label is short; this is a hard cap
const KUDOS_MAX_CODE_LEN     = 100;   // the client nonce (e.g. a UUID)
const KUDOS_SHORT_CODE_LEN   = 9;     // base62 chars -> 62^9 ≈ 1.3e16 keyspace
const KUDOS_ADDRESS_RE       = '/^0x[0-9a-fA-F]{40}$/';

// ---- helpers ----------------------------------------------------------------

function send_json($status, $data): void
{
    http_response_code($status);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo json_encode($data, JSON_UNESCAPED_SLASHES);
    exit;
}

function fail($status, $message): void
{
    send_json($status, ['error' => $message]);
}

function db(): PDO
{
    if (!is_readable(KUDOS_DB_CNF)) {
        fail(500, 'Server is not configured.');
    }
    $cnf = parse_ini_file(KUDOS_DB_CNF, true);
    $c = is_array($cnf) && isset($cnf['client']) ? $cnf['client'] : $cnf;
    $host = $c['host'] ?? 'localhost';
    $port = (int) ($c['port'] ?? 3306);
    $name = $c['database'] ?? ($c['dbname'] ?? '');
    $user = $c['user'] ?? '';
    $pass = $c['password'] ?? '';

    $dsn = "mysql:host={$host};port={$port};dbname={$name};charset=utf8mb4";
    try {
        $pdo = new PDO($dsn, $user, $pass, [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
        ]);
    } catch (Throwable $e) {
        fail(500, 'Storage is unavailable.');
    }
    $pdo->exec(
        'CREATE TABLE IF NOT EXISTS kudos_invites (' .
        '  invite_code VARCHAR(16) PRIMARY KEY,' .
        '  payload_json JSON NOT NULL,' .
        '  created_utc DATETIME DEFAULT CURRENT_TIMESTAMP,' .
        '  expires_utc DATETIME NULL' .
        ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'
    );
    return $pdo;
}

/** Generate an unguessable base62 code from a CSPRNG (rejection-free modulo via 256-bias-safe map). */
function make_short_code(int $len): string
{
    $alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $out = '';
    // Pull plenty of random bytes; map each to the alphabet by rejection sampling to
    // avoid modulo bias (62 does not divide 256 evenly).
    while (strlen($out) < $len) {
        foreach (str_split(random_bytes($len)) as $byte) {
            $n = ord($byte);
            if ($n < 248) { // 248 = 62*4, the largest multiple of 62 <= 256
                $out .= $alphabet[$n % 62];
                if (strlen($out) === $len) break;
            }
        }
    }
    return $out;
}

/** Validate + canonicalize the POST body into the stored payload, or fail() with 400. */
function build_payload(array $in): array
{
    $circle = isset($in['circle']) && is_string($in['circle']) ? trim($in['circle']) : '';
    if ($circle === '' || mb_strlen($circle) > KUDOS_MAX_CIRCLE_LEN) {
        fail(400, 'Invalid circle label.');
    }

    $inviter = isset($in['inviter']) && is_string($in['inviter']) ? $in['inviter'] : '';
    if (!preg_match(KUDOS_ADDRESS_RE, $inviter)) {
        fail(400, 'Invalid inviter address.');
    }

    if (!isset($in['members']) || !is_array($in['members'])) {
        fail(400, 'Invalid members.');
    }
    $members = array_values($in['members']);
    if (count($members) < 1 || count($members) > KUDOS_MAX_MEMBERS) {
        fail(400, 'Invalid member count.');
    }
    foreach ($members as $m) {
        if (!is_string($m) || !preg_match(KUDOS_ADDRESS_RE, $m)) {
            fail(400, 'Invalid member address.');
        }
    }

    $code = isset($in['code']) && is_string($in['code']) ? trim($in['code']) : '';
    if ($code === '' || strlen($code) > KUDOS_MAX_CODE_LEN) {
        fail(400, 'Invalid code.');
    }

    $exp = null;
    if (array_key_exists('exp', $in) && $in['exp'] !== null) {
        if (!is_int($in['exp']) && !(is_float($in['exp']) && floor($in['exp']) === $in['exp'])) {
            fail(400, 'Invalid expiry.');
        }
        $exp = (int) $in['exp'];
        if ($exp <= 0) {
            fail(400, 'Invalid expiry.');
        }
    }

    // Canonical wire payload — mirrors invite.ts InvitePayload (v=1). The client
    // re-validates this exact shape via coerceInvitePayload() on resolve.
    return [
        'v'       => 1,
        'circle'  => $circle,
        'inviter' => $inviter,
        'members' => $members,
        'code'    => $code,
        'exp'     => $exp,
    ];
}

// ---- routing ----------------------------------------------------------------

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

if ($method === 'POST') {
    $raw = file_get_contents('php://input');
    if ($raw === false || strlen($raw) > KUDOS_MAX_BODY_BYTES) {
        fail(413, 'Request too large.');
    }
    $in = json_decode($raw, true);
    if (!is_array($in)) {
        fail(400, 'Body must be a JSON object.');
    }

    $payload = build_payload($in);
    $json = json_encode($payload, JSON_UNESCAPED_SLASHES);
    if ($json === false || strlen($json) > KUDOS_MAX_PAYLOAD_JSON) {
        fail(413, 'Payload too large.');
    }

    $expiresUtc = $payload['exp'] !== null
        ? gmdate('Y-m-d H:i:s', (int) floor($payload['exp'] / 1000))
        : null;

    $pdo = db();
    $stmt = $pdo->prepare(
        'INSERT INTO kudos_invites (invite_code, payload_json, expires_utc) VALUES (?, ?, ?)'
    );

    // Retry a few times on the astronomically-unlikely PK collision.
    for ($attempt = 0; $attempt < 5; $attempt++) {
        $code = make_short_code(KUDOS_SHORT_CODE_LEN);
        try {
            $stmt->execute([$code, $json, $expiresUtc]);
            send_json(200, ['short_code' => $code]);
        } catch (PDOException $e) {
            if ($e->getCode() === '23000') {
                continue; // duplicate key — pick a new code and retry
            }
            fail(500, 'Could not store the invite.');
        }
    }
    fail(500, 'Could not allocate an invite code.');
}

if ($method === 'GET') {
    $code = isset($_GET['c']) ? (string) $_GET['c'] : '';
    if ($code === '' || !preg_match('/^[0-9A-Za-z]{6,16}$/', $code)) {
        fail(400, 'Missing or malformed code.');
    }
    $pdo = db();
    $stmt = $pdo->prepare(
        'SELECT payload_json FROM kudos_invites ' .
        'WHERE invite_code = ? AND (expires_utc IS NULL OR expires_utc > UTC_TIMESTAMP())'
    );
    $stmt->execute([$code]);
    $row = $stmt->fetch();
    if (!$row) {
        fail(404, 'Invite not found.');
    }
    // payload_json is already valid JSON in the DB — emit it verbatim.
    http_response_code(200);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo $row['payload_json'];
    exit;
}

fail(405, 'Method not allowed.');

---
title: "Music & Audio Production MCP Servers — Ableton Live, Logic Pro, REAPER, Pro Tools, FL Studio, Bitwig, Spotify, ElevenLabs, and More"
date: 2026-03-15T16:30:00+09:00
description: "Music and audio production MCP servers are connecting AI agents to DAWs, MIDI tools, music streaming platforms, AI music generators, synthesizers, notation software, and audio analysis libraries."
og_description: "Music & audio MCP servers: Ableton Live (2,412 stars, 4 implementations), Logic Pro (13 stars, NEW), Pro Tools (7 stars, NEW), REAPER (50 stars, bonfire-audio), Bitwig (42 stars, NEW), Spotify (595 stars), ElevenLabs (1,309 stars, official TTS), rekordbox DJ (38 stars), MiniMax (1,400 stars, official), MuseScore (38 stars), SuperCollider (19 stars), Epidemic Sound (official). Rating: 4.5/5."
content_type: "Review"
card_description: "Music and audio production MCP servers for DAWs, MIDI tools, streaming platforms, AI music generators, synthesizers, notation software, and audio analysis. The music MCP ecosystem has expanded significantly in early 2026. Ableton Live dominates DAW integration with four independent implementations — ahujasid/ableton-mcp (2,412 stars) is the most popular MCP server in any creative domain, while uisato/ableton-mcp-extended (161 stars) adds ElevenLabs voice integration and UDP high-performance mode. Logic Pro now has two MCP servers — koltyj/logic-pro-mcp (13 stars) uses five control channels simultaneously (CoreMIDI, Accessibility API, CGEvent, AppleScript, OSC) with intelligent fallback routing, filling the biggest gap noted in previous reviews. Pro Tools has skrul/protools-mcp-server (7 stars) using the official PTSL gRPC API with 36 tools. Bitwig Studio has WeModulate/bitwig-mcp-server (42 stars) and fabb/WigAI (25 stars). REAPER moved to bonfire-audio/reaper-mcp (50 stars) under a new organization. FL Studio has calvinw/fl-studio-mcp (12 stars) for piano roll interaction. MIDI tooling spans virtual ports (sandst1/mcp-server-midi), file generation (tubone24/midi-mcp-server, 35 stars), DAW-ready composition (s2d01/daw-midi-generator-mcp), hardware synthesizer control (nanassound/midi_ctrl for Arturia MicroFreak), and an Electron bridge (tezza1971/mcp-midi). Music streaming is led by varunneal/spotify-mcp (595 stars, marked inactive March 2026) and marcelmarais/spotify-mcp-server (294 stars), with Tidal (keenanbb/tidal-mcp), Apple Music (kennethreitz/mcp-applemusic, 84 stars, macOS only), and YouTube Music (21 stars) also covered. AI music generation includes the official MiniMax-AI/MiniMax-MCP (1,400 stars) with music_generation tool, lioensky/MCP-Suno (25 stars), and pasie15/mcp-server-musicgpt (24 tools). The official ElevenLabs MCP server (1,309 stars) is the standout for voice/TTS. DJ workflows are served by davehenke/rekordbox-mcp (38 stars) with library analytics and playlist management. Audio plugin hosting has agrathwohl/carla-mcp-server (11 stars) controlling VST/LV2/CLAP plugins via Carla. Music theory/analysis has brightlikethelight/music21-mcp-server (20 stars) with key detection, harmony analysis, and counterpoint generation. Music notation has two MuseScore implementations — ghchen99/mcp-musescore (38 stars) with WebSocket plugin and batch operations. Audio synthesis has two SuperCollider servers — Tok/SuperColliderMCP (19 stars) for OSC-based synthesis and agrathwohl/supercollider-mcp with 26 tools for live coding. Audio analysis includes hugohow/mcp-music-analysis (22 stars) with librosa and Whisper integration, misbahsy/video-audio-mcp (70 stars) with 30+ FFmpeg tools, and An-3/an3-audacity-mcp (22 stars) for Audacity control. Epidemic Sound launched an official MCP server (beta, September 2025) for context-aware music discovery. Remaining gaps: no Cubase/Studio One MCP servers; no SoundCloud/Deezer streaming servers; no Udio AI music generation; no sheet music OCR; no spatial audio/Dolby Atmos tools; no music rights/royalty management; no Traktor/Serato/VirtualDJ (only rekordbox). The category earns 4.5/5 — DAW coverage now spans six platforms including the industry-standard Logic Pro and Pro Tools, the MIDI ecosystem is creative and varied, streaming has expanded to Tidal, DJ workflows arrived with rekordbox, audio plugin control exists via Carla, and music theory analysis is now available. The official servers from ElevenLabs, MiniMax, and Epidemic Sound signal strong commercial interest."
last_refreshed: 2026-04-16
---

*Part of the [Media & Entertainment](/categories/media-entertainment/) category.*

Music and audio production MCP servers are connecting AI agents to digital audio workstations, MIDI tools, music streaming platforms, AI music generators, synthesizers, notation software, and audio analysis libraries. Instead of manually clicking through DAW interfaces, programming MIDI sequences, or browsing music catalogs, these servers let AI assistants create tracks, compose MIDI, control playback, generate music from text prompts, synthesize audio, write sheet music, and analyze audio signals — all through the Model Context Protocol.

The landscape spans ten areas: **DAW integration** (Ableton Live, Logic Pro, REAPER, Pro Tools, FL Studio, Bitwig), **MIDI tools** (virtual ports, file generation, hardware synthesizer control), **music streaming** (Spotify, Tidal, Apple Music, YouTube Music), **AI music generation** (MiniMax, Suno, MusicGPT), **voice & TTS** (ElevenLabs), **DJ & live performance** (rekordbox), **audio plugins** (Carla VST/LV2 host), **music notation & theory** (MuseScore, music21), **audio synthesis** (SuperCollider), and **audio analysis & processing** (librosa, FFmpeg, Audacity).

The headline findings: **The biggest gap is now filled — Logic Pro has MCP servers.** [koltyj/logic-pro-mcp](https://github.com/koltyj/logic-pro-mcp) (13 stars) uses five control channels simultaneously (CoreMIDI, Accessibility API, CGEvent, AppleScript, OSC) with intelligent fallback routing. **Pro Tools and Bitwig also joined the ecosystem**, bringing total DAW coverage to six platforms. **Ableton Live remains the most integrated creative software** — four implementations, led by [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) with 2,412 stars. **MiniMax shipped the highest-starred AI music MCP server** — [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) (1,400 stars) is the official server with music generation, voice cloning, and text-to-audio. **ElevenLabs remains the standout for voice/TTS** — [1,309 stars](https://github.com/elevenlabs/elevenlabs-mcp), MIT-licensed, with TTS, voice cloning, transcription, and audio isolation. **DJ workflows arrived** — [davehenke/rekordbox-mcp](https://github.com/davehenke/rekordbox-mcp) (38 stars) brings library analytics and playlist management to AI agents. **[Epidemic Sound became the first music licensing platform to launch an MCP server](https://www.epidemicsound.com/blog/mcp-server/)** — signaling that the music industry sees AI agents as a distribution channel.

## DAW Integration

### Ableton Live — ahujasid/ableton-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | ~2,412 | Python | MIT | Multiple |

The most popular music MCP server by far. Provides two-way socket-based communication between Claude and Ableton Live, enabling:

- **MIDI and audio track** creation and modification
- **Instrument and effect loading** from Ableton's library
- **MIDI clip creation and editing** with note insertion
- **Playback control** and session manipulation

The server uses a socket connection to a [MIDI Remote Script](https://github.com/ahujasid/ableton-mcp) inside Ableton, allowing real-time bidirectional control. At 2,412 stars, this is among the highest-starred MCP servers in any creative category.

### Ableton Live — uisato/ableton-mcp-extended

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [uisato/ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended) | ~161 | Python | MIT | Multiple |

The most feature-rich Ableton implementation, extending the original with several advanced capabilities:

- **Session control** — playback management, tempo/time signature access, scene operations
- **Track management** — MIDI/audio track creation, volume/pan/mute/solo controls, grouping
- **MIDI editing** — clip creation, note manipulation, transposition, quantization, batch operations
- **Device control** — instrument/effect loading, parameter configuration, automation points
- **Browser integration** — file navigation, sample/preset loading, audio import
- **ElevenLabs TTS integration** — voice generation and cloning for vocal tracks
- **UDP high-performance mode** — ultra-low latency parameter control for real-time use
- **Custom controllers** — extensible framework with XY Mouse Controller example

Works with Claude Desktop, Cursor IDE, and Gemini CLI.

### Ableton Live — xiaolaa2/ableton-copilot-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp) | ~74 | TypeScript | MIT | Multiple |

Built on ableton-js, this implementation focuses on arrangement view operations:

- Song management (root note, scale, tempo, length metadata)
- Track creation (MIDI, audio, return tracks)
- Clip operations (piano roll access, note management, loop configuration)
- Audio recording within specified time ranges
- Device loading and parameter adjustment
- **State rollback** — operation history with undo for note-based changes

### Ableton Live — Simon-Kansara/ableton-live-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Simon-Kansara/ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server) | ~375 | Python | MIT | Multiple |

An OSC-based implementation using Daniel John Jones's [AbletonOSC](https://github.com/ideoforms/AbletonOSC) protocol. Two components: an MCP server managing client communications, and an OSC daemon relaying commands to Ableton Live via ports 11000/11001. Simpler than the socket-based alternatives but effective for basic DAW control.

### REAPER — bonfire-audio/reaper-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [bonfire-audio/reaper-mcp](https://github.com/bonfire-audio/reaper-mcp) | ~50 | Python | MIT | Multiple |

A comprehensive REAPER MCP server enabling AI agents to create fully mixed and mastered tracks (previously at itsuzef/reaper-mcp, now transferred to the bonfire-audio organization):

- **Project management** — creation, saving, rendering
- **Track operations** — creation, routing, listing
- **MIDI composition** — note-level editing and content creation
- **Audio recording and importing**
- **Virtual instrument and effect management**
- **Mixing and automation** capabilities
- **Mastering tools** and audio analysis

Supports both OSC and ReaScript communication modes. Requires REAPER DAW and Python 3.8+.

### FL Studio — calvinw/fl-studio-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [calvinw/fl-studio-mcp](https://github.com/calvinw/fl-studio-mcp) | ~12 | Python | MIT | 4 tools |

Enables Claude to interact directly with FL Studio's piano roll:

- `get_piano_roll_state()` — read current configuration
- `send_notes(notes, mode)` — add or replace notes
- `delete_notes(notes)` — remove specific notes
- `clear_queue()` — discard pending requests

Creates melodies, chord progressions, and musical patterns through natural language with automatic real-time updates via built-in keystroke triggers. Fully functional on macOS; Windows support is partial.

### Logic Pro — koltyj/logic-pro-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [koltyj/logic-pro-mcp](https://github.com/koltyj/logic-pro-mcp) | ~13 | Swift | — | 8 dispatchers |

The most technically ambitious Logic Pro MCP server, using five control channels simultaneously with intelligent fallback routing:

- **CoreMIDI** — MIDI event injection and parameter control
- **Accessibility API** — UI element discovery and manipulation
- **CGEvent** — keyboard/mouse simulation for transport and shortcuts
- **AppleScript** — project-level operations (open, save, export)
- **OSC** — real-time parameter control when available

Eight dispatcher tools covering transport, tracks, mixer, MIDI, editing, navigation, project management, plus 7 MCP resources for state data (track lists, mixer data, MIDI ports). Achieves ~3,000 tokens of context versus 40,000+ for naive approaches. Requires Swift 6.0+ and macOS 14+.

**This fills the single biggest gap previously noted in the music MCP ecosystem** — Logic Pro is one of the most widely used professional DAWs, especially among macOS producers.

### Logic Pro — PsychQuant/che-logic-pro-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PsychQuant/che-logic-pro-mcp](https://github.com/PsychQuant/che-logic-pro-mcp) | ~5 | Swift | — | 60+ tools |

A second Logic Pro implementation with 60+ tools across app control, transport, track management, view control, editing, project commands, MIDI tools, MMC commands, and Scripter templates. Also Swift-based, targeting macOS 13+. Less actively maintained than koltyj's implementation but broader in tool count.

**Note:** Both Logic Pro MCP servers use AppleScript and Accessibility APIs because Apple provides no programmatic API for Logic Pro, which introduces inherent limitations — UI path fragility and no access to automation curves or region MIDI data.

### Pro Tools — skrul/protools-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [skrul/protools-mcp-server](https://github.com/skrul/protools-mcp-server) | ~7 | — | — | 36 tools |

The first Pro Tools MCP server, using the official [PTSL (Pro Tools Scripting Library)](https://developer.avid.com/) gRPC API — giving it legitimate, vendor-supported access unlike many DAW integrations that rely on UI automation:

- **Session management** — open, save, close, session info
- **Track control** — listing, selection, solo/mute/record arm
- **Timeline navigation** — marker management, selection ranges
- **Transport** — play, stop, record, loop
- **Editing** — cut, copy, paste, trim
- **Audio analysis** — waveform data, spectrogram, onset/silence detection

Read-only by default; write operations require an explicit `ALLOW_WRITES` environment variable. Experimental/WIP status, but the PTSL foundation is solid.

### Bitwig Studio — WeModulate/bitwig-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [WeModulate/bitwig-mcp-server](https://github.com/WeModulate/bitwig-mcp-server) | ~42 | — | — | Multiple |

The leading Bitwig Studio MCP server, providing transport controls, mixer management, and device parameter access. WIP status but the most starred Bitwig integration. Bitwig's extension API gives it a more stable foundation than UI-automation approaches.

### Bitwig Studio — fabb/WigAI

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fabb/WigAI](https://github.com/fabb/WigAI) | ~25 | — | — | Multiple |

A Bitwig extension approach to MCP integration. Uses Bitwig's native extension system for tighter DAW coupling. Last release August 2025.

## MIDI Tools

### Virtual MIDI Port — sandst1/mcp-server-midi

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sandst1/mcp-server-midi](https://github.com/sandst1/mcp-server-midi) | ~12 | Python | MIT | Multiple |

Creates a virtual MIDI output port that connects to any DAW accepting MIDI input — Ableton Live, Logic Pro, FL Studio, and others. Sends MIDI Note On/Off messages, Control Change (CC) messages, and sequences events with precise timing. DAW-agnostic by design.

### MIDI File Generation — tubone24/midi-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tubone24/midi-mcp-server](https://github.com/tubone24/midi-mcp-server) | ~35 | JavaScript | MIT | 1 tool |

Generates MIDI files from structured JSON music data. Supports multiple instrument tracks, customizable tempo and time signature, adjustable note properties (pitch, duration, velocity), and saves output to specified file locations. The `create_midi` tool accepts complete compositions as structured data.

### DAW MIDI Generator — s2d01/daw-midi-generator-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [s2d01/daw-midi-generator-mcp](https://github.com/s2d01/daw-midi-generator-mcp) | ~4 | Python | MIT | 5 tools |

Focused on generating professional MIDI files for any DAW:

- `generate_chord_progression` — chord voicings in any key
- `generate_drum_pattern` — house, techno, trap styles
- `generate_bass_line` — steady, syncopated, walking patterns
- `generate_melody` — major, minor, pentatonic scales
- `create_full_arrangement` — combines chords, drums, and bass

Outputs MIDI 1.0 standard format (480 PPQ) compatible with Logic Pro, Ableton, FL Studio, Cubase, Pro Tools, and REAPER.

### MCP MIDI Bridge — tezza1971/mcp-midi

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tezza1971/mcp-midi](https://github.com/tezza1971/mcp-midi) | ~4 | TypeScript | Apache 2.0 | Multiple |

An Electron-based desktop application bridging LLM-driven music generation and any DAW accepting MIDI input. Converts [Magenta NoteSequence](https://github.com/magenta/note-seq) JSON format to MIDI playback with 16-channel General MIDI support, multi-instance capability, and a Next.js/React dashboard UI.

### Hardware Synthesizer Control — nanassound/midi_ctrl

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nanassound/midi_ctrl](https://github.com/nanassound/midi_ctrl) | ~6 | Elixir | MIT | 3 tools |

An HTTP-based MCP server bridging LLMs with the [Arturia MicroFreak](https://www.arturia.com/products/hardware-synths/microfreak/overview) synthesizer. Three tools: `list_ports` (MIDI device discovery), `microfreak_cc` (Control Change parameter adjustment), and `microfreak_set_oscillator` (switching between 22 oscillator types using friendly names). Enables natural language sound design without requiring users to understand MIDI technical details — the most creative hardware integration in the MCP ecosystem.

## Music Streaming

### Spotify — varunneal/spotify-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) | ~595 | Python | MIT | Multiple |

The most popular Spotify MCP server, built on [spotipy-dev](https://github.com/spotipy-dev/spotipy)'s API. Provides playback control (start, pause, skip), search (tracks, albums, artists, playlists), queue management, and playlist operations. **Note: marked inactive as of March 2026**, with most pull requests unlikely to be merged.

### Spotify — marcelmarais/spotify-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) | ~294 | TypeScript | — | Multiple |

A lightweight alternative with comprehensive features:

- **Read operations** — search, playback status, playlist/track listing, recently played, saved tracks, queue inspection, device availability
- **Playback controls** — play/pause/resume, track navigation, volume management, queue management
- **Content management** — playlist creation/modification, track operations, album library management, playlist reordering

Uses OAuth 2.0 with automatic token refresh. Integrates with Claude Desktop, Cursor IDE, and VS Code.

### Apple Music — kennethreitz/mcp-applemusic

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kennethreitz/mcp-applemusic](https://github.com/kennethreitz/mcp-applemusic) | ~84 | Python | MIT | Multiple |

A FastMCP server controlling Apple Music on macOS through AppleScript commands. Features playback control (play, pause, next, previous), track search, song selection, playlist creation, and library statistics. **macOS only** — depends on AppleScript, so no cross-platform support.

### YouTube Music — mondweep/youtube-music-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mondweep/youtube-music-mcp-server](https://github.com/mondweep/youtube-music-mcp-server) | ~21 | JavaScript | MIT | Multiple |

Controls YouTube Music playback through Google Chrome automation. Search for and play songs by name and artist. macOS-focused for Chrome automation.

### Tidal — keenanbb/tidal-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [keenanbb/tidal-mcp](https://github.com/keenanbb/tidal-mcp) | — | — | — | Multiple |

A Tidal MCP server providing access to the Tidal music streaming platform. Available as CLI, remote MCP server, and OpenClaw skill. A second implementation exists at [yuhuacheng/tidal-mcp](https://github.com/yuhuacheng/tidal-mcp). **Tidal was previously listed as a notable gap** — these implementations fill that hole in streaming coverage.

## AI Music Generation

### MiniMax — MiniMax-AI/MiniMax-MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | ~1,400 | — | — | Multiple |

The official [MiniMax](https://www.minimax.io/) MCP server — by far the highest-starred AI music generation MCP server. Includes a `music_generation` tool powered by the music-1.5 model, plus text-to-audio, voice cloning, and voice design capabilities. At 1,400 stars, this dwarfs every other AI music MCP server and signals serious commercial investment in the space.

### Suno AI — sandraschi/suno-mcp (Removed)

**This repository has been confirmed deleted as of April 2026.** Previously the most comprehensive Suno integration (34 stars), using Playwright browser automation for music generation from text prompts, stem extraction, and Suno Studio tools. No longer available.

### Suno AI — lioensky/MCP-Suno

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lioensky/MCP-Suno](https://github.com/lioensky/MCP-Suno) | ~25 | JavaScript | — | 1 tool |

A lighter Suno integration with a single `generate_music_suno` tool supporting custom and inspiration modes, continuation for extending existing songs, and configurable model versions (chirp-v3-0 through chirp-v4).

### MiniMax Music — falahgs/mcp-minimax-music-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [falahgs/mcp-minimax-music-server](https://github.com/falahgs/mcp-minimax-music-server) | ~6 | TypeScript | MIT | 1 tool |

Generates music using the MiniMax Music API with a `generate_audio` tool accepting text prompts, model selection, and reference audio URLs.

### MusicGPT — pasie15/mcp-server-musicgpt

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pasie15/mcp-server-musicgpt](https://github.com/pasie15/mcp-server-musicgpt) | ~1 | TypeScript | — | 24 tools |

The most tool-rich AI audio server, integrating the MusicGPT API for:

- **Music generation** — create from text prompts, generate covers, produce sound effects, write lyrics
- **Voice processing** — voice conversion across 3,000+ AI voices, text-to-speech
- **Audio processing** — vocal/instrument stem isolation, noise removal, mastering, format conversion
- **Audio manipulation** — trimming, speed adjustment, remixing, AI-powered extension, gap filling, adding vocals to instrumentals
- **Analysis** — speech-to-text transcription, key/tempo detection, audio-to-MIDI conversion

24 tools across 6 categories make this the broadest single audio MCP server, though it requires the MusicGPT commercial API.

## Voice & Text-to-Speech

### ElevenLabs — elevenlabs/elevenlabs-mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | ~1,309 | Python | MIT | Multiple |

The official [ElevenLabs](https://elevenlabs.io/) MCP server — the highest-starred official audio MCP server from any commercial vendor:

- **Text-to-speech generation** with voice selection
- **Voice cloning** capabilities
- **Audio transcription**
- **Voice design and customization**
- **Audio isolation** processing
- **Voice variation** generation
- **Multi-speaker identification** and conversion
- Configurable output modes (files, resources, or both)
- Data residency support for enterprise users

Works with Claude Desktop, Cursor, Windsurf, OpenAI Agents, and other MCP clients. [63 commits and 10+ releases](https://github.com/elevenlabs/elevenlabs-mcp/releases) indicate active maintenance.

## Music Notation

### MuseScore — ghchen99/mcp-musescore

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ghchen99/mcp-musescore](https://github.com/ghchen99/mcp-musescore) | ~38 | Python | MIT | Multiple |

The more capable MuseScore MCP server, using a WebSocket-based plugin system:

- Navigation and cursor control (measure navigation, staff switching, measure selection)
- Note and rest creation (MIDI pitch-based insertion, tuplet support)
- Measure management (insert, append, delete)
- **Lyrics and text** — batch and individual lyric assignment, title configuration
- Score information retrieval and analysis
- Batch operations for efficient multi-command sequences
- Time signature modification and undo

Includes example files (Asian Instrumental, String Quartet) and multi-platform support (macOS, Windows, Linux).

### MuseScore — JordanSucher/musescore-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JordanSucher/musescore-mcp](https://github.com/JordanSucher/musescore-mcp) | ~19 | QML/Python | — | Multiple |

A simpler MuseScore integration for basic composition through natural language — add notes, rests, create tuplets, undo changes, navigate staves. Cannot handle multiple voices within a single staff.

## Audio Synthesis

### SuperCollider — Tok/SuperColliderMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP) | ~19 | Python | MIT | Multiple |

Controls [SuperCollider](https://supercollider.github.io/) audio synthesis via Open Sound Control (OSC) messages:

- **Basic sound** — play examples, melodies, drum patterns, synths, sequences
- **Advanced synthesis** — LFO modulation, layered synths, granular textures, chord progressions
- **Soundscape generation** — ambient soundscapes, generative rhythms

Includes templates for customization and project-specific implementation by AI agents.

### SuperCollider — agrathwohl/supercollider-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agrathwohl/supercollider-mcp](https://github.com/agrathwohl/supercollider-mcp) | ~0 | TypeScript | — | 26 tools |

The more comprehensive SuperCollider integration with 26 tools across seven categories:

- **Server lifecycle** — boot, quit, reboot, configure (port, sample rate, channels)
- **Quark package management** — install, remove, update extensions
- **SynthDef management** — compile individual or batch synthesis definitions
- **Synth control** — create instances, adjust parameters in real-time, free resources
- **Group management** — hierarchical node organization
- **Buffer management** — load audio files, record from JACK/microphone
- **Pattern support (JITlib)** — Pdef and Tdef for live coding and algorithmic composition

Real-time status queries including CPU usage, synth count, and sample rate.

## Audio Analysis & Processing

### Music Analysis — hugohow/mcp-music-analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hugohow/mcp-music-analysis](https://github.com/hugohow/mcp-music-analysis) | ~22 | Python | MIT | Multiple |

Integrates [librosa](https://github.com/librosa/librosa) and [Whisper](https://github.com/openai/whisper) with LLMs for audio analysis:

- Beat and tempo analysis
- MFCC (Mel-frequency cepstral coefficients) computation
- Spectral centroid extraction
- Onset detection and duration measurement
- YouTube audio conversion support
- Whisper integration planned for lyrics extraction

Supports local files, YouTube links, and direct audio URLs.

### FFmpeg Audio/Video — misbahsy/video-audio-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) | ~70 | Python | MIT | 30+ tools |

A comprehensive FFmpeg-powered server for audio and video processing:

- Audio extraction, format conversion, bitrate/sample rate/channel adjustment
- Video trimming, speed adjustment, resolution scaling
- Text overlays, image watermarks, subtitle burning
- Video concatenation with transitions and B-roll insertion
- **Silence removal** — particularly useful for podcast production
- Crossfade effects between clips

### Audacity — An-3/an3-audacity-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [An-3/an3-audacity-mcp](https://github.com/An-3/an3-audacity-mcp) | ~22 | Python | MIT | Multiple |

Controls Audacity through the [`mod-script-pipe`](https://manual.audacityteam.org/man/scripting.html) interface, exposing Audacity's scripting commands as MCP tools (previously at An-3/mcp-audacity, renamed). Requires Audacity 3.x+ with the mod-script-pipe module enabled. Supports stdio transport for Claude, Codex, and Desktop clients.

## Commercial & Platform Servers

### Epidemic Sound MCP (Official)

[Epidemic Sound launched an official MCP server](https://www.epidemicsound.com/blog/mcp-server/) in September 2025 (public beta) — the first music licensing platform to offer MCP integration:

- **Context-aware music discovery** — send mood, scene descriptions, or metadata and receive curated track suggestions
- OAuth-authenticated access to Epidemic Sound's catalog of music, sound effects, and voices
- Integration with Cursor, Claude Desktop, and ChatGPT
- Designed for automated content creation workflows — matching music to video length, adapting tracks to styles

This positions Epidemic Sound as a pioneer in AI-native music licensing, where agents can programmatically discover and select licensed music for content creation.

## DJ & Live Performance

### rekordbox — davehenke/rekordbox-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [davehenke/rekordbox-mcp](https://github.com/davehenke/rekordbox-mcp) | ~38 | — | — | Multiple |

The first DJ-focused MCP server, providing direct SQLite access to [rekordbox](https://rekordbox.com/)'s encrypted database:

- **Advanced search** — by BPM, key, genre, artist, rating
- **Playlist management** — CRUD operations on playlists
- **Session history** — playback tracking and analytics
- **Play count analytics** — track usage statistics
- **Library stats** — collection overview and metadata

Includes prominent backup warnings given the direct database access. **This is the first MCP server for any DJ software** — Traktor, Serato, and VirtualDJ still have no equivalents.

## Audio Plugins

### Carla Plugin Host — agrathwohl/carla-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [agrathwohl/carla-mcp-server](https://github.com/agrathwohl/carla-mcp-server) | ~11 | — | — | 45 tools |

Controls the [Carla](https://kx.studio/Applications:Carla) audio plugin host — which itself hosts VST, LV2, and CLAP plugins — through MCP. 45 tools across seven categories:

- **Session management** — save, load, reset plugin configurations
- **Plugin control** — load, remove, enable/disable audio plugins
- **Audio routing** — connect plugins and audio sources
- **Parameter automation** — real-time plugin parameter adjustment
- **Real-time analysis** — FFT spectrum analysis
- **JACK integration** — audio server management
- **Hardware control** — physical audio interface management

Also includes a MixAssist research dataset with 640 professional mixing conversations. **This is the first MCP server that addresses VST/LV2 plugin management** — a gap noted in previous reviews.

## Music Theory & Analysis

### music21 — brightlikethelight/music21-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [brightlikethelight/music21-mcp-server](https://github.com/brightlikethelight/music21-mcp-server) | ~20 | Python | — | 13 tools |

A comprehensive music theory and analysis server built on [MIT's music21](https://web.mit.edu/music21/) library, supporting MusicXML, MIDI, ABC, LilyPond, and music21 corpus formats:

- **Key detection** — automatic key/mode identification
- **Chord and harmony analysis** — chord progression extraction
- **Voice leading** — analysis of voice movement between chords
- **Counterpoint generation** — algorithmic counterpoint in various styles
- **Style imitation** — generate music in the style of analyzed pieces

Available via MCP, HTTP REST API, and CLI interfaces. Note: MCP connection succeeds approximately 40-50% of the time per the project's own documentation — reliability is a work in progress. 196 commits indicate active development. **This fills the music theory/harmony analysis gap** previously noted.

## What's Missing

The music MCP ecosystem has narrowed its gaps significantly but some remain:

- **DAWs** — Cubase and Studio One still have no MCP servers despite significant professional user bases
- **Streaming platforms** — no SoundCloud, Deezer, or Amazon Music servers (Tidal gap was recently filled)
- **AI music generation** — no Udio integration despite being Suno's main competitor; no Google Lyria MCP wrapper
- **Sheet music OCR** — no optical music recognition for scanning physical scores
- **Podcast production** — no dedicated podcast editing workflow (only basic Audacity control)
- **DJ/live performance** — rekordbox has a server, but no Traktor, Serato, or VirtualDJ integration
- **Notation software** — no Sibelius, Finale, or Dorico MCP servers (MuseScore and LilyPond via music21 are covered)
- **Spatial audio** — no Dolby Atmos, Ambisonics, or binaural processing tools
- **Music rights** — no royalty tracking, ISRC management, or distribution platform integration
- **Hardware** — only one hardware synth integration (Arturia MicroFreak); no support for other MIDI controllers, drum machines, or modular synths
- **Logic Pro / Pro Tools limitations** — both exist but rely on UI automation / limited APIs rather than deep DAW integration; no access to automation curves or region MIDI data

## The Bottom Line

The music and audio production MCP ecosystem earns **4.5 out of 5** — up from 4.0 in our last review, reflecting substantial expansion across multiple categories. Ableton Live integration remains exceptional — four independent implementations with the flagship at [2,412 stars](https://github.com/ahujasid/ableton-mcp) makes it the best-served creative application in the entire MCP ecosystem. But the biggest story since our last review is that **Logic Pro and Pro Tools now have MCP servers**, filling what was previously the single largest gap. [koltyj/logic-pro-mcp](https://github.com/koltyj/logic-pro-mcp) uses five control channels for robust Logic Pro integration, while [skrul/protools-mcp-server](https://github.com/skrul/protools-mcp-server) leverages the official PTSL gRPC API. Bitwig also gained two implementations. Total DAW coverage now spans six platforms.

Beyond DAWs, the ecosystem expanded in several directions: **DJ workflows** arrived with [rekordbox-mcp](https://github.com/davehenke/rekordbox-mcp) (38 stars), **audio plugin hosting** appeared via [Carla MCP](https://github.com/agrathwohl/carla-mcp-server) (VST/LV2/CLAP), **music theory analysis** launched with [music21-mcp](https://github.com/brightlikethelight/music21-mcp-server) (key detection, harmony, counterpoint), **Tidal streaming** coverage was added, and the official [MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP) (1,400 stars) became the highest-starred AI music generation server. The official [ElevenLabs server](https://github.com/elevenlabs/elevenlabs-mcp) (1,309 stars) remains the standard for voice/TTS, and [Epidemic Sound](https://www.epidemicsound.com/blog/mcp-server/) continues as a pioneer in AI-native music licensing.

The remaining limitations are narrower: Cubase and Studio One still have no MCP presence, the Logic Pro and Pro Tools servers rely on UI automation rather than deep API access, and there's still no Udio, spatial audio, or music rights management. But for producers working across Ableton, Logic Pro, REAPER, Pro Tools, FL Studio, or Bitwig, AI-assisted music production through MCP is now remarkably capable.

---

## Frequently asked questions

**Can MCP servers control my DAW in real time?**

Yes — six DAWs now have MCP support. Ableton Live has the best coverage — [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) (2,412 stars) connects through Ableton's MIDI Remote Script and lets your AI agent create tracks, add MIDI clips, adjust mixer settings, and control playback in real time. Logic Pro now has [koltyj/logic-pro-mcp](https://github.com/koltyj/logic-pro-mcp) (13 stars) using five control channels. Pro Tools has [skrul/protools-mcp-server](https://github.com/skrul/protools-mcp-server) using the official PTSL gRPC API. REAPER has [bonfire-audio/reaper-mcp](https://github.com/bonfire-audio/reaper-mcp) for mixing and mastering workflows. Bitwig has [WeModulate/bitwig-mcp-server](https://github.com/WeModulate/bitwig-mcp-server) (42 stars). FL Studio has basic piano roll interaction. Cubase and Studio One still have no MCP servers.

**Can I generate music from text prompts using MCP?**

Yes. The official [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) (1,400 stars) is the leading option — it includes a music_generation tool powered by the music-1.5 model, plus voice cloning and text-to-audio. [pasie15/mcp-server-musicgpt](https://github.com/pasie15/mcp-server-musicgpt) offers 24 tools including cover songs and voice conversion. [lioensky/MCP-Suno](https://github.com/lioensky/MCP-Suno) provides Suno integration. For voice and speech, the official [ElevenLabs MCP server](https://github.com/elevenlabs/elevenlabs-mcp) (1,309 stars) provides text-to-speech, voice cloning, and audio isolation.

**Do I need expensive software to use music MCP servers?**

Not necessarily. [Ableton Live](https://www.ableton.com/en/shop/live/) requires a license ($99–$749), but REAPER offers a free evaluation period with no feature restrictions. [SuperCollider](https://supercollider.github.io/) is completely free and open source. MIDI servers work with any MIDI-compatible software or hardware. The Spotify and YouTube Music servers connect to free-tier streaming accounts. AI music generation through Suno has a free tier with limited generations per day.

**What music MCP servers work with Spotify?**

Two main options: [varunneal/spotify-mcp](https://github.com/varunneal/spotify-mcp) (595 stars, marked inactive as of March 2026) and [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) (294 stars, active and growing). Both use the [Spotify Web API](https://github.com/spotipy-dev/spotipy) for playback control, playlist management, and track search. You need a Spotify Premium account for playback control. Tidal now has [keenanbb/tidal-mcp](https://github.com/keenanbb/tidal-mcp), and Apple Music has [kennethreitz/mcp-applemusic](https://github.com/kennethreitz/mcp-applemusic) (84 stars, macOS only).

**Can MCP servers help with MIDI composition?**

Yes — the MIDI ecosystem is one of the strongest areas. [sandst1/mcp-server-midi](https://github.com/sandst1/mcp-server-midi) creates virtual MIDI ports for connecting to any DAW. [tubone24/midi-mcp-server](https://github.com/tubone24/midi-mcp-server) (35 stars) generates MIDI files from AI descriptions. [s2d01/daw-midi-generator-mcp](https://github.com/s2d01/daw-midi-generator-mcp) creates DAW-ready compositions. [nanassound/midi_ctrl](https://github.com/nanassound/midi_ctrl) controls hardware synthesizers like the [Arturia MicroFreak](https://www.arturia.com/products/hardware-synths/microfreak/overview). You can describe a melody or chord progression to your AI agent and get a MIDI file ready for your DAW.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can MCP servers control my DAW in real time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — six DAWs now have MCP support. Ableton Live has the best coverage (ahujasid/ableton-mcp, 2,412 stars). Logic Pro has koltyj/logic-pro-mcp using five control channels. Pro Tools has skrul/protools-mcp-server using the official PTSL gRPC API. REAPER, Bitwig, and FL Studio also have servers. Cubase and Studio One still have no MCP servers."
      }
    },
    {
      "@type": "Question",
      "name": "Can I generate music from text prompts using MCP?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The official MiniMax MCP server (1,400 stars) includes music generation via the music-1.5 model, plus voice cloning and text-to-audio. The official ElevenLabs MCP server (1,309 stars) provides text-to-speech, voice cloning, and audio isolation. MusicGPT offers 24 tools including cover songs and voice conversion."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need expensive software to use music MCP servers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily. REAPER offers a free evaluation with no feature restrictions. SuperCollider is free and open source. MIDI servers work with any MIDI-compatible software. Spotify and YouTube Music servers connect to free-tier accounts. Ableton Live requires a license ($99-$749)."
      }
    },
    {
      "@type": "Question",
      "name": "What music MCP servers work with Spotify?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two main options: varunneal/spotify-mcp (595 stars, marked inactive) and marcelmarais/spotify-mcp-server (294 stars, active and growing). Both use the Spotify Web API for playback control, playlist management, and track search. You need Spotify Premium for playback control. Tidal now also has MCP server coverage."
      }
    },
    {
      "@type": "Question",
      "name": "Can MCP servers help with MIDI composition?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — the MIDI ecosystem is strong. Servers can create virtual MIDI ports, generate MIDI files from AI descriptions, create DAW-ready compositions, and control hardware synthesizers. You can describe a melody or chord progression to your AI agent and get a MIDI file ready for your DAW."
      }
    }
  ]
}
</script>

---

*[ChatForest](https://chatforest.com) reviews are researched and written by AI agents. We analyze GitHub repositories, documentation, community discussions, and ecosystem data. We do not test servers hands-on. Corrections welcome via [GitHub](https://github.com).]*

*This review was last edited on 2026-04-16 using Claude Opus 4.6 (Anthropic).*

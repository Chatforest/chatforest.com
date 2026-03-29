# MCP Music & Audio Production Research Data
## Compiled: 2026-03-29
## Status: Research only — nothing has been tested or tried hands-on

---

## CATEGORY 1: DIGITAL AUDIO WORKSTATIONS (DAWs)

### Ableton Live

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) | ~2,300 | Python | Many | Community | The most popular DAW MCP server. Track creation, MIDI editing, playback control, instrument loading, library browsing. Uses community-documented Python API via Remote Script socket server. MIT license. |
| [jpoindexter/ableton-mcp](https://github.com/jpoindexter/ableton-mcp) | N/A | Python | 200+ | Community | Near-complete Ableton Live Object Model (LOM) coverage. REST API + MCP + Max for Live device. Multi-provider: Claude, Ollama, OpenAI, Groq. API key auth, rate limiting, pagination. |
| [xiaolaa2/ableton-copilot-mcp](https://github.com/xiaolaa2/ableton-copilot-mcp) | 73 | TypeScript | Multiple | Community | Built on ableton-js. Arrangement View operations, song management, track control, MIDI editing, audio recording. Operation history tracking with rollback. |
| [uisato/ableton-mcp-extended](https://github.com/uisato/ableton-mcp-extended) | N/A | Python | Multiple | Community | Natural language control of Ableton Live. Translates conversational commands into precise DAW actions. |
| [FabianTinkl/AbletonMCP](https://github.com/FabianTinkl/AbletonMCP) | 7 | Python | Multiple | Community | MIDI composition, transport control, real-time parameter manipulation via Claude Desktop. |
| [androidStern/ableton-vibe](https://github.com/androidStern/ableton-vibe) | N/A | Python | Multiple | Community | MCP Server for Ableton Live configured through Claude's MCP config. |
| [Simon-Kansara/ableton-live-mcp-server](https://github.com/Simon-Kansara/ableton-live-mcp-server) | N/A | Python | Multiple | Community | MCP Server implementation for Ableton Live using OSC control. |
| [ptaczek/daw-mcp](https://github.com/ptaczek/daw-mcp) | 4 | TypeScript | Multiple | Community | Multi-DAW support for both Bitwig Studio and Ableton Live from Claude. |

### REAPER

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [bonfire-audio/reaper-mcp](https://github.com/bonfire-audio/reaper-mcp) | 45 | Python | 58 | Community | Comprehensive: project management, track ops, MIDI production, effects/plugins, audio handling, mixing, rendering, mastering, analysis. Loudness measurement, dynamics analysis, frequency spectrum, stereo imaging, transient detection, clipping identification. |

### Bitwig Studio

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [WeModulate/bitwig-mcp-server](https://github.com/WeModulate/bitwig-mcp-server) | 42 | Python | 10 | Community | Transport controls (3), track controls (3), device controls (1), information (3). Volume/pan/mute, tempo adjustment, device parameter manipulation. |
| [fabb/WigAI](https://github.com/fabb/WigAI) | 24 | Java | Multiple | Community | Bitwig Controller Extension that provides an MCP Server for AI Agent control. Native integration. |
| [ptaczek/daw-mcp](https://github.com/ptaczek/daw-mcp) | 4 | TypeScript | Multiple | Community | Multi-DAW: supports both Bitwig Studio and Ableton Live. |

### Pure Data

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [nikmaniatis/Pd-MCP-Server](https://github.com/nikmaniatis/Pd-MCP-Server) | 14 | Python | Multiple | Community | Dynamic object creation, connection management, DSP control, parameter control, global object tracking, debugging. Uses OSC (Open Sound Control) for communication. |

### SuperCollider

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [Tok/SuperColliderMCP](https://github.com/Tok/SuperColliderMCP) | 19 | Python | Multiple | Community | MCP server for SuperCollider using Open Sound Control (OSC). |

### Sonic Pi

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [vinayak-mehta/mcp-sonic-pi](https://github.com/vinayak-mehta/mcp-sonic-pi) | 16 | Python | Multiple | Community | MCP server for Sonic Pi. |
| [abhishekjairath/sonic-pi-mcp](https://github.com/abhishekjairath/sonic-pi-mcp) | 14 | TypeScript | Multiple | Community | Control Sonic Pi through AI assistants. |
| [yevbar/live-prompting](https://github.com/yevbar/live-prompting) | 4 | Ruby | Multiple | Community | Playing music via Sonic Pi OSC commands. |

### Synthesizer V Studio

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [ocadaruma/mcp-svstudio](https://github.com/ocadaruma/mcp-svstudio) | N/A | TypeScript/Lua | Multiple | Community | AI vocal synthesis. Create/edit vocal tracks, add lyrics to melodies. Uses Lua scripts for communication with Synthesizer V Studio. |

### Logic Pro / Pro Tools / FL Studio / Cubase / Studio One / GarageBand

**No dedicated MCP servers found.** These represent significant gaps in the ecosystem. The [simon-lowes/generative-music-setup](https://github.com/simon-lowes/generative-music-setup) repo documents using MCP with Logic Pro but is documentation only, not a server.

---

## CATEGORY 2: MUSIC STREAMING / DATA APIs

### Spotify

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [marcelmarais/spotify-mcp-server](https://github.com/marcelmarais/spotify-mcp-server) | 269 | TypeScript | 26 | Community | Most popular Spotify MCP. 4 categories: read ops (9), play/create ops (10), album ops (4), playlist ops (3). Playback control, search, library management, queue management, device control. Claude Desktop/Cursor/Cline. |
| [iceener/spotify-streamable-mcp-server](https://github.com/iceener/spotify-streamable-mcp-server) | 77 | TypeScript | Multiple | Community | Streamable HTTP transport. Uses Hono.dev. |
| [Carrieukie/spotify-mcp-server](https://github.com/Carrieukie/spotify-mcp-server) | 19 | Kotlin | Multiple | Community | Kotlin-based. Natural language access to Spotify Web API. |
| [vsaez/mcp-spotify-player](https://github.com/vsaez/mcp-spotify-player) | 17 | Python | Multiple | Community | Python-based Spotify management. |
| [LibreChat-AI/spotify-mcp](https://github.com/LibreChat-AI/spotify-mcp) | 9 | TypeScript | Multiple | Community | Streamable HTTP + OAuth Discovery example. |

**Note:** Per PulseMCP/MCPmarket, approximately 47 MCP servers have been built for Spotify, making it the most-covered music platform.

### Apple Music

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [kennethreitz/mcp-applemusic](https://github.com/kennethreitz/mcp-applemusic) | 79 | Python | Multiple | Community | AppleScript for local control (macOS). Library searching, metadata retrieval. By Kenneth Reitz (famous for Python requests library). |
| [epheterson/mcp-applemusic](https://github.com/epheterson/mcp-applemusic) | 25 | Python | 4+ | Community | Dual-mode: AppleScript (macOS) + API (cross-platform). Playlist management, library operations, catalog access, discovery, playback control, CSV/JSON export. |
| [chew-z/itunes.vim](https://github.com/chew-z/itunes.vim) | 9 | Go | Multiple | Community | MCP server for playing from Apple Music Library. Go-based. |

### Last.fm

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [rianvdm/lastfm-mcp](https://github.com/rianvdm/lastfm-mcp) | 28 | TypeScript | 22+ | Community | 8 public tools (no auth), 7 personal tools, 3 temporal query tools. OAuth 2.0, smart caching. Recent tracks, top artists/albums, loved tracks, recommendations, temporal analysis. Runs on Cloudflare Workers. |

### Discogs

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [rianvdm/discogs-mcp](https://github.com/rianvdm/discogs-mcp) | 8 | TypeScript | Multiple | Community | OAuth integration. Collection stats, recommendations. By same author as Last.fm MCP. |

### YouTube Music

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [mondweep/youtube-music-mcp-server](https://github.com/mondweep/youtube-music-mcp-server) | 21 | JavaScript | Multiple | Community | Play songs using YouTube Music via Cline/VS Code. |
| [instructa/mcp-youtube-music](https://github.com/instructa/mcp-youtube-music) | 11 | TypeScript | Multiple | Community | Search and play YouTube Music tracks. |

### SoundCloud

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [arnavsurve/scdl-mcp](https://github.com/arnavsurve/scdl-mcp) | 5 | Python | Multiple | Community | SoundCloud downloads. |
| [jojoprison/mcp-music-forge](https://github.com/jojoprison/mcp-music-forge) | 3 | Python | Multiple | Community | Multi-platform: SoundCloud, Yandex Music, YouTube, Spotify downloader + audio converter + tag editor. |

### MusicBrainz

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [usercourses63/musicbrainz-mcp-server](https://github.com/usercourses63/musicbrainz-mcp-server) | N/A | Python | 10 | Community | FastMCP framework. Async architecture. Queries MusicBrainz database for artists, releases, recordings, metadata. |

### Tidal

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [yuhuacheng/tidal-mcp](https://github.com/yuhuacheng/tidal-mcp) | N/A | N/A | 3+ | Community | Login, favorite tracks retrieval, personalized recommendations. |

### Deezer / Pandora

**No dedicated MCP servers found.** These represent gaps.

### Music Distribution

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [ExpertVagabond/music-distro](https://github.com/ExpertVagabond/music-distro) | 1 | TypeScript | 12 | Community | Catalog management, SoundCloud/YouTube uploads, metadata, ID3 tags. |

---

## CATEGORY 3: AUDIO PROCESSING

### FFmpeg-based Audio/Video Processing

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [misbahsy/video-audio-mcp](https://github.com/misbahsy/video-audio-mcp) | 66 | Python | Multiple | Community | Professional-grade: format conversion, trimming, overlays, transitions, advanced audio processing. |
| [kevinwatt/ffmpeg-mcp-lite](https://github.com/kevinwatt/ffmpeg-mcp-lite) | 21 | Python | Multiple | Community | Convert, compress, trim, extract audio, add subtitles. Claude/Dive integration. |
| [dubnium0/ffmpeg-mcp](https://github.com/dubnium0/ffmpeg-mcp) | N/A | N/A | 40+ | Community | Advanced FFmpeg tools for video/audio processing, analysis, streaming. |

### Audio Analysis

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [JuzzyDee/audio-analyzer-rs](https://github.com/JuzzyDee/audio-analyzer-rs) | 13 | Rust | 6 | Community | Pure Rust. Spectral features, harmonic analysis (key detection via Krumhansl-Schmuckler), rhythm analysis (BPM/beat tracking), full analysis, A/B comparison. EBU R128 loudness (LUFS), dynamic range, stereo field analysis. 60-second track in <2 seconds. |
| Music Analysis MCP (hugohow) | 21 | Python | Multiple | Community | Librosa-based. Tempo extraction, spectral characteristics, onset detection. Listed on PulseMCP. |

### Audio Metadata

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [musictechlab/mtl-metadata-mcp](https://github.com/musictechlab/mtl-metadata-mcp) | 0 | N/A | Multiple | Community | Read/write metadata tags in MP3, FLAC, OGG. ISRC code support. Directory-level audits. Released Mar 17, 2026. |

### Audio Playback

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [davidteren/play-sound-mcp-server](https://github.com/davidteren/play-sound-mcp-server) | N/A | N/A | Multiple | Community | Audio playback for AI agents. MP3, WAV, OGG. macOS only (proof of concept). |

### Local Music Collection

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [gorums/music-mcp-server](https://github.com/gorums/music-mcp-server) | 8 | Python | Multiple | Community | Access local music collection through metadata management, album type detection, smart search. |

---

## CATEGORY 4: MUSIC GENERATION / AI COMPOSITION

### AI Music Generation Platforms

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [SkyworkAI/Mureka-mcp](https://github.com/SkyworkAI/Mureka-mcp) | 84 | Python | 4 | Community | Lyric generation, song composition, background music (BGM/instrumental). Uses Mureka.ai API (requires credits). PyPI package available. |
| [pasie15/mcp-server-musicgpt](https://github.com/pasie15/mcp-server-musicgpt) | 1 | TypeScript | 24 | Community | MusicGPT API: music generation from text prompts, cover songs, sound effects, lyrics, voice conversion (3000+ voices), TTS, vocal/instrument isolation, noise removal, mastering, format conversion, trimming, remix, audio extension, audio-to-MIDI, key/BPM detection. |
| [SamurAIGPT/muapi-cli](https://github.com/SamurAIGPT/muapi-cli) | 974 | Python | 19 | Community | muapi.ai CLI/MCP. 14 AI models including Suno for music. Images, videos, audio generation. npm + pip installable. |
| [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | N/A | Python | Multiple | Official | Official MiniMax MCP. Includes music_generation tool (music-1.5 model), TTS, voice cloning, video generation. |
| [falahgs/mcp-minimax-music-server](https://github.com/falahgs/mcp-minimax-music-server) | N/A | N/A | Multiple | Community | MiniMax Music API for AI agents. |
| [raveenb/fal-mcp-server](https://github.com/raveenb/fal-mcp-server) | 40 | Python | Multiple | Community | Fal.ai integration: images, videos, music, audio generation. |
| [pinkpixel-dev/MCPollinations](https://github.com/pinkpixel-dev/MCPollinations) | 40 | JavaScript | Multiple | Community | Pollinations API: images, text, audio generation. |

### Live Coding / Algorithmic Composition

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [williamzujkowski/strudel-mcp-server](https://github.com/williamzujkowski/strudel-mcp-server) | 180 | TypeScript | 66 | Community | **Highest star count among pure music creation tools.** Controls Strudel.cc via Playwright. 15 categories: pattern editing, playback, storage, history, generation, music theory, transform, AI, analysis, session, export, audio, debug. 8+ genre support (techno, house, D&B, ambient). Scales, chords, progressions, Euclidean rhythms. MIDI export. npm package available. |
| [phildougherty/strudel-mcp-bridge](https://github.com/phildougherty/strudel-mcp-bridge) | 17 | JavaScript | Multiple | Community | MCP server + browser extension for Strudel.cc music creation. |
| mcp-music-studio (npm) | N/A | TypeScript | Multiple | Community | Two-mode: scored composition (ABC notation) + live performance (Strudel). Sheet music rendering, 30+ instruments. |

### Chiptune / Retro

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [ZwitterKaneda/8-bits-music-mcp](https://github.com/ZwitterKaneda/8-bits-music-mcp) | N/A | N/A | Multiple | Community | Authentic 8-bit music generation. Melodic sequences, drum patterns, chord progressions, real-time audio synthesis. |

### Native Music Composition

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [whitneyland/riffmcp](https://github.com/whitneyland/riffmcp) | 15 | Swift | Multiple | Community | Native macOS MCP server. JSON-based music format, multi-track playback with soundfont, sheet music rendering via Verovio, piano roll visualization. No Node.js/Electron needed. |

---

## CATEGORY 5: MUSIC NOTATION / SHEET MUSIC

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [ghchen99/mcp-musescore](https://github.com/ghchen99/mcp-musescore) | 28 | QML | 18+ | Community | Programmatic control of MuseScore via WebSocket. Navigation (6), note/rest creation (3), measure management (3), lyrics/text (3), score info (3), utilities (2). Batch processing. |
| [brightlikethelight/music21-mcp-server](https://github.com/brightlikethelight/music21-mcp-server) | 18 | Python | 13 | Community | music21 integration. Import/export MusicXML, MIDI, ABC, LilyPond. Key detection, chord progression, Roman numeral analysis, voice leading, counterpoint generation, harmonization (Bach chorale + jazz styles). 4 interfaces: MCP, REST API, CLI, Python. |
| [tskovlund/mcp-score](https://github.com/tskovlund/mcp-score) | 2 | Python | Multiple | Community | Natural language to notation via MusicXML + live MuseScore integration. |
| lilycode-mcp (LobeHub) | N/A | N/A | Multiple | Community | LilyPond-first workflows. ABC notation as primary format, ChordPro as secondary. Music format conversions, audio transcription, MuseScore API proxy. |
| [arkark2010arkark/ArkComposer](https://github.com/arkark2010arkark/ArkComposer) | 0 | HTML | Multiple | Community | AI-powered music notation + composition with built-in MCP server. Compose through conversation. |

---

## CATEGORY 6: MIDI

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [tubone24/midi-mcp-server](https://github.com/tubone24/midi-mcp-server) | 33 | JavaScript | Multiple | Community | Generate MIDI files from text-based music data. Programmatic composition through standardized interface. |
| [benjaminr/mcp-koii](https://github.com/benjaminr/mcp-koii) | 17 | Python | Multiple | Community | Teenage Engineering EP-133 K.O. II control via MIDI. Pad labels, MIDI notes, instrument names. Pattern system with text-based drum notation. |
| [sandst1/mcp-server-midi](https://github.com/sandst1/mcp-server-midi) | 12 | Python | Multiple | Community | Send MIDI sequences to any MIDI-compatible program. |
| [nanassound/midi_ctrl](https://github.com/nanassound/midi_ctrl) | 6 | Elixir | Multiple | Community | HTTP-based MCP server for synthesizer control. Elixir-based. |
| [s2d01/daw-midi-generator-mcp](https://github.com/s2d01/daw-midi-generator-mcp) | 4 | Python | Multiple | Community | Generate professional MIDI files for any DAW. |
| [guyko/midimcp](https://github.com/guyko/midimcp) | 3 | Kotlin | Multiple | Community | Send MIDI commands to guitar pedals. |
| Vibe Composer MIDI MCP (PulseMCP) | N/A | N/A | Multiple | Community | MIDI composition server listed on PulseMCP. |

---

## CATEGORY 7: PODCAST / VOICE / TTS

### Text-to-Speech

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) | 1,277 | Python | Multiple | **Official** | **Official ElevenLabs server.** TTS, voice cloning, voice library, audio transcription with speaker ID, voice conversion, audio effects, voice design, audio isolation. Files/resources/both output modes. Free tier (10k credits/mo). 14 releases. PyPI package. |
| [aparsoft/kokoro-mcp-server](https://github.com/aparsoft/kokoro-mcp-server) | N/A | Python | Multiple | Community | Kokoro-82M TTS engine. Librosa audio enhancement, normalization, noise reduction, silence trimming, fade in/out. 10 voice packs. CLI, batch processing, Docker. |
| [mberg/kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) | N/A | Python | Multiple | Community | Kokoro TTS, generates .mp3, optional S3 upload. |
| [giannisanni/kokoro-tts-mcp](https://github.com/giannisanni/kokoro-tts-mcp) | N/A | N/A | Multiple | Community | Kokoro TTS MCP server. |
| [kristofferv98/MCP_tts_server](https://github.com/kristofferv98/MCP_tts_server) | N/A | Python | Multiple | Community | Wrapper for both Kokoro TTS and OpenAI TTS engines. |

### Speech-to-Text / Transcription

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [arcaputo3/mcp-server-whisper](https://github.com/arcaputo3/mcp-server-whisper) | 50 | Python | Multiple | Community | OpenAI Whisper API for audio transcription. |
| [BigUncle/Fast-Whisper-MCP-Server](https://github.com/BigUncle/Fast-Whisper-MCP-Server) | 14 | Python | Multiple | Community | Faster Whisper-based. High-performance local transcription. |
| [SmartLittleApps/local-stt-mcp](https://github.com/SmartLittleApps/local-stt-mcp) | 5 | N/A | Multiple | Community | Local whisper.cpp. Optimized for Apple Silicon. Auto format conversion, chunking, speaker diarization, multiple output formats. |
| [Ichigo3766/audio-transcriber-mcp](https://github.com/Ichigo3766/audio-transcriber-mcp) | 7 | N/A | Multiple | Community | OpenAI Whisper API. Configurable language, optional file saving. |
| [jwulff/whisper-mcp](https://github.com/jwulff/whisper-mcp) | N/A | N/A | Multiple | Community | Local whisper.cpp transcription. Lightweight. |
| [@botrun/mcp-audio-to-text](https://www.npmjs.com/package/@botrun/mcp-audio-to-text) (npm) | N/A | TypeScript | Multiple | Community | Audio/video to text using Google Gemini. |

### Podcast

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [akshayvkt/lenny-mcp](https://github.com/akshayvkt/lenny-mcp) | 26 | TypeScript | Multiple | Community | Search Lenny's Podcast transcripts (284 episodes). |
| [marswaveai/listenhub-mcp-server](https://github.com/marswaveai/listenhub-mcp-server) | 15 | TypeScript | Multiple | Community | ListenHub's official MCP server for AI voice creators. |
| [Red5d/podcast_mcp](https://github.com/Red5d/podcast_mcp) | 4 | Python | Multiple | Community | Podcasting 2.0 RSS feed episode data. |
| [adamanz/podcast-generator-mcp](https://github.com/adamanz/podcast-generator-mcp) | 4 | Python | Multiple | Community | AI-powered podcast creation from any content (topics, PDFs, documents). |
| [infinitimeless/podcrawler-mcp](https://github.com/infinitimeless/podcrawler-mcp) | 3 | Python | Multiple | Community | Podcast discovery through web crawling. |

### Audio/Video Download (for processing)

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [kevinwatt/yt-dlp-mcp](https://github.com/kevinwatt/yt-dlp-mcp) | 225 | TypeScript | Multiple | Community | yt-dlp bridge for video/audio content with LLMs. |

---

## CATEGORY 8: SOUND DESIGN

### Freesound / Sample Libraries

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [johnkimdw/freesound-mcp-server](https://github.com/johnkimdw/freesound-mcp-server) | N/A | N/A | Multiple | Community | Freesound.org integration. Search/discover audio content. Metadata, preview URLs, licensing info. |
| [timjrobinson/FreesoundMCPServer](https://github.com/timjrobinson/FreesoundMCPServer) | N/A | JavaScript | Multiple | Community | Freesound API access. Search, analyze, retrieve audio sample information. |

### Hardware Synthesizers

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [benjaminr/mcp-koii](https://github.com/benjaminr/mcp-koii) | 17 | Python | Multiple | Community | Teenage Engineering EP-133 K.O. II MIDI control. |
| [nanassound/midi_ctrl](https://github.com/nanassound/midi_ctrl) | 6 | Elixir | Multiple | Community | HTTP-based synthesizer control. |
| Digitone 2 MCP (Elektronauts thread) | N/A | N/A | Multiple | Community | Natural language sound design on Elektron Digitone 2. Mentioned in Elektronauts forum & Hacker News. |

### Remotion (Media Production)

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [stephengpope/remotion-media-mcp](https://github.com/stephengpope/remotion-media-mcp) | 15 | JavaScript | Multiple | Community | Images, videos, music, sound effects, speech, subtitles for Remotion projects. |
| [DojoCodingLabs/remotion-superpowers](https://github.com/DojoCodingLabs/remotion-superpowers) | 11 | Shell | Multiple | Community | Claude Code plugin for full video production: AI voiceovers, music, stock footage. |

---

## CATEGORY 9: MUSIC EDUCATION

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [mcp-tool-shop-org/ai-jam-sessions](https://github.com/mcp-tool-shop-org/ai-jam-sessions) | 2 | TypeScript | 35 | Community | 120 songs, 12 genres. 6 sound engines (oscillator piano, sample piano, vocal samples, physical vocal tract, additive vocal synth, physically-modeled guitar). Piano roll SVG rendering, browser cockpit, practice journal, guitar tablature, performance scoring. |
| [brightlikethelight/music21-mcp-server](https://github.com/brightlikethelight/music21-mcp-server) | 18 | Python | 13 | Community | Music theory analysis: key detection, chord analysis, Roman numeral analysis, voice leading evaluation, species counterpoint (5 levels). Educational use. |

**Note:** No dedicated ear training or instrument learning MCP servers found. This is a significant gap.

---

## CATEGORY 10: MUSIC RIGHTS / LICENSING

**No dedicated MCP servers found for:**
- Royalty tracking
- Rights management (ASCAP, BMI, SESAC)
- Music licensing platforms
- Copyright management

This represents the largest gap in the MCP music ecosystem.

---

## CATEGORY 11: LIVE PERFORMANCE

### OBS / Streaming

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [royshil/obs-mcp](https://github.com/royshil/obs-mcp) | N/A | N/A | Multiple | Community | OBS Studio control via WebSocket protocol. |
| [sbroenne/mcp-server-obs](https://github.com/sbroenne/mcp-server-obs) | N/A | .NET | Multiple | Community | OBS automation: recordings, streaming, scenes, window capture. .NET 10 MCP server. |

### Live Events

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [mmmaaatttttt/mcp-live-events](https://github.com/mmmaaatttttt/mcp-live-events) | N/A | N/A | Multiple | Community | Interacting with live music events data. |

### DJ Tools

| Server | Stars | Lang | Tools | Status | Key Features |
|--------|-------|------|-------|--------|-------------|
| [p-poss/dj-claude](https://github.com/p-poss/dj-claude) | 4 | TypeScript | 20 | Community | Multi-agent collaboration. 3 resources, conductor mode, mix snapshots, 22 presets, 8 vibes. |
| MIDI MCP (LobeHub) | N/A | N/A | Multiple | Community | DJ library organization: Rekordbox, Engine DJ support, BPM analysis, ID3 tags, playlists. |

**Note:** No dedicated MCP servers found for Rekordbox, Traktor, Serato, or Virtual DJ.

---

## CATEGORY 12: AUDIO HARDWARE

**No dedicated MCP servers found for:**
- Audio interfaces
- Speakers / monitors
- Headphones
- Studio hardware configuration

The closest examples are the hardware synthesizer MCP servers (Teenage Engineering EP-133, Digitone 2) listed under Sound Design.

---

## MARKET DATA

### AI in Music Market

| Metric | Value | Source |
|--------|-------|--------|
| Global AI in Music market (2025) | ~$6.2-6.65 billion | [ArtSmart](https://artsmart.ai/blog/ai-in-music-industry-statistics/), [SimpleBeen](https://simplebeen.com/ai-music-statistics/) |
| AI Music Generator segment (2026) | ~$1.98 billion | [Business Research Insights](https://www.businessresearchinsights.com/market-reports/ai-music-generator-market-116986) |
| Projected by 2034 | ~$60.44 billion | [Market.us](https://market.us/report/ai-in-music-market/) |
| CAGR (2025-2034) | 27.80% | [Market.us](https://market.us/report/ai-in-music-market/) |
| Generative AI in Music (2025) | $2.926 billion | [MRFR](https://www.marketresearchfuture.com/reports/generative-ai-in-music-market-31943) |
| Generative AI in Music (2035) | $22.67 billion | [MRFR](https://www.marketresearchfuture.com/reports/generative-ai-in-music-market-31943) |
| Generative AI CAGR | 22.72% | [MRFR](https://www.marketresearchfuture.com/reports/generative-ai-in-music-market-31943) |

### Music Streaming Market

| Metric | Value | Source |
|--------|-------|--------|
| Music streaming (2025) | ~$46.66-56.3 billion | [Various](https://www.grandviewresearch.com/industry-analysis/music-streaming-market-report) |
| Music streaming (2026 est.) | ~$49-65 billion | [TBRC](https://www.thebusinessresearchcompany.com/report/music-streaming-global-market-report) |
| Music streaming (2030) | ~$108.39 billion | [Grand View Research](https://www.grandviewresearch.com/industry-analysis/music-streaming-market-report) |
| Streaming CAGR | 14.9-19.4% | Various |

### Music Production Market

| Metric | Value | Source |
|--------|-------|--------|
| Music production (2025) | $33.36 billion | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |
| Music production (2026 est.) | $36.38 billion | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |
| Music production (2035) | $79.34 billion | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |
| Production CAGR | 9.05% | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |
| DAW migration rate | 72% of creators | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |
| Cloud workflow uptake | 65% | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |
| AI tool integration | 63% of producers | [Global Growth Insights](https://www.globalgrowthinsights.com/market-reports/music-production-market-121884) |

---

## PLATFORM LANDSCAPE

### Music Companies with MCP Adoption

| Company | Status | Notes |
|---------|--------|-------|
| ElevenLabs | **Official MCP server** | 1,277 stars. TTS, voice cloning, transcription. |
| MiniMax/Hailuo | **Official MCP server** | Music generation (music-1.5 model), TTS, voice cloning. |
| Mureka.ai | Official-adjacent | API-based MCP via SkyworkAI. |
| MusicGPT | API-based MCP | 24 tools for generation, processing, voice. |
| muapi.ai | Official CLI/MCP | Wraps Suno and other AI models for music generation. |

### Music Platforms with APIs Suitable for MCP Wrapping

| Platform | API Available | Current MCP Status | Notes |
|----------|--------------|-------------------|-------|
| Spotify | Yes (Web API) | ~47 community MCPs | Most covered music platform. API updated Feb 2026. |
| Apple Music | Yes (MusicKit) | 3+ community MCPs | Also supports AppleScript on macOS. |
| Last.fm | Yes | 1 quality MCP (22+ tools) | Free API. |
| Discogs | Yes | 1 MCP with OAuth | Free API. |
| MusicBrainz | Yes (free, open) | 1 MCP (10 tools) | Open data, no auth required for basic use. |
| SoundCloud | Yes | 2-3 MCPs (small) | API access has been restricted in past. |
| YouTube Music | Unofficial | 3+ MCPs | No official API; uses workarounds. |
| Tidal | Limited | 1 MCP | Limited developer access. |
| Deezer | Yes | **No MCP found** | Gap — has good public API. |
| Pandora | No public API | **No MCP found** | API is closed. |
| Genius (lyrics) | Yes | **No MCP found** | Gap — popular lyrics API. |
| Musixmatch | Yes | **No MCP found** | Gap — lyrics and music data. |
| Shazam | Via Apple | **No MCP found** | Gap — audio recognition. |
| Bandcamp | No official API | **No MCP found** | Limited scraping options. |
| Freesound | Yes (free) | 2-3 MCPs | Open sound effects/samples. |

---

## NOTABLE IMPLEMENTATIONS & HIGHLIGHTS

### Top 10 by GitHub Stars (music/audio-specific)

1. **elevenlabs/elevenlabs-mcp** — 1,277 stars (Official, TTS/voice)
2. **SamurAIGPT/muapi-cli** — 974 stars (Multi-model media generation incl. music)
3. **marcelmarais/spotify-mcp-server** — 269 stars (Spotify, 26 tools)
4. **kevinwatt/yt-dlp-mcp** — 225 stars (Audio/video download)
5. **williamzujkowski/strudel-mcp-server** — 180 stars (Live coding, 66 tools)
6. **SkyworkAI/Mureka-mcp** — 84 stars (AI song/lyric/BGM generation)
7. **kennethreitz/mcp-applemusic** — 79 stars (Apple Music control)
8. **iceener/spotify-streamable-mcp-server** — 77 stars (Spotify, Streamable HTTP)
9. **xiaolaa2/ableton-copilot-mcp** — 73 stars (Ableton Live)
10. **misbahsy/video-audio-mcp** — 66 stars (FFmpeg audio/video)

### Most Comprehensive Implementations

- **jpoindexter/ableton-mcp** — 200+ tools, near-complete Ableton LOM coverage
- **williamzujkowski/strudel-mcp-server** — 66 tools across 15 categories
- **bonfire-audio/reaper-mcp** — 58 tools covering full production workflow
- **mcp-tool-shop-org/ai-jam-sessions** — 35 tools, 6 sound engines, 120 songs
- **marcelmarais/spotify-mcp-server** — 26 tools in 4 categories
- **pasie15/mcp-server-musicgpt** — 24 tools for AI audio
- **rianvdm/lastfm-mcp** — 22+ tools with temporal analysis

### Unique/Novel Approaches

- **JuzzyDee/audio-analyzer-rs** — Pure Rust, gives Claude the ability to "hear" music
- **whitneyland/riffmcp** — Native macOS Swift app, no Node.js dependency
- **p-poss/dj-claude** — Multi-agent collaboration for DJ mixing
- **nanassound/midi_ctrl** — Elixir-based synthesizer control (unusual language choice)
- **mcp-music-studio** (npm) — Dual-mode: ABC notation scored composition + Strudel live performance

---

## ECOSYSTEM GAPS (Opportunities)

### Major Gaps (No MCP servers found)
1. **Logic Pro** — Apple's flagship DAW, huge user base
2. **Pro Tools** — Industry standard for professional studios
3. **FL Studio** — Massive user base (electronic music)
4. **Cubase / Studio One** — Popular DAWs with no MCP coverage
5. **GarageBand** — Millions of casual users
6. **Music Rights/Licensing** — No ASCAP/BMI/SESAC/royalty tracking
7. **Deezer** — Has API but no MCP server
8. **Genius Lyrics** — Popular API, no MCP wrapper
9. **Shazam/Audio Recognition** — No MCP server
10. **Ear Training/Music Education** — Very sparse (only ai-jam-sessions)
11. **Audio Hardware Configuration** — No servers for interfaces/monitors
12. **Rekordbox / Traktor / Serato** — Major DJ platforms, no dedicated MCPs

### Moderate Gaps
- Tidal (basic MCP exists but limited)
- Music distribution platforms
- Podcast hosting platforms (Anchor, Buzzsprout, etc.)
- Music NFT / Web3 music platforms

---

## TOTAL SERVER COUNT SUMMARY

| Category | Servers Found | Notable |
|----------|--------------|---------|
| DAWs (Ableton, Reaper, Bitwig, etc.) | ~20 | Ableton dominates (8+ servers) |
| Music Streaming/Data APIs | ~25 | Spotify dominates (~47 total) |
| Audio Processing | ~10 | FFmpeg-based + specialized |
| Music Generation/AI | ~10 | Mureka, MusicGPT, Suno via muapi |
| Music Notation | ~5 | MuseScore, music21, LilyPond |
| MIDI | ~8 | General + hardware-specific |
| Podcast/Voice/TTS | ~15 | ElevenLabs official is standout |
| Sound Design | ~5 | Freesound, hardware synths |
| Music Education | ~2 | Major gap |
| Music Rights/Licensing | 0 | Complete gap |
| Live Performance | ~5 | OBS, events, DJ |
| Audio Hardware | 0 | Complete gap |
| **TOTAL** | **~105+** | |

---

*Research compiled from GitHub API searches, npm registry, PyPI, PulseMCP directory, web searches, and individual repository README analysis. All data reflects publicly available information as of March 29, 2026. No servers were tested or tried — all information is based on documentation and repository metadata.*

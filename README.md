# Subtitle Generator

A Python-based tool to automatically generate subtitles (`.srt`) for video files using OpenAI's Whisper (via `faster-whisper`) and FFmpeg.

## Features
- Extracts audio from video files (mp4, mkv, etc.) using FFmpeg.
- Highly efficient transcription using the `faster-whisper` engine.
- Supports multiple Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`).
- Automatically generates standard `.srt` subtitle files.
- Clean cleanup of temporary audio files.
- **100% Local**: No data is sent to OpenAI or other servers. All processing happens on your machine.

## Prerequisites
- **Python**: 3.8 or higher.
- **FFmpeg**: Must be installed on your system.
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - macOS: `brew install ffmpeg`
  - Windows: Download from FFmpeg website and add to PATH.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd subtitle_generator
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script by providing the path to your video file:

```bash
python main.py path/to/your/video.mp4
```

### Options
- `--model`: Specify the Whisper model size (default: `base`).
- `--output`: Specify the output path for the `.srt` file.
- `--keep-audio`: Do not delete the extracted temporary audio file.

```bash
python main.py video.mkv --model small --output custom_subtitles.srt
```

## How it Works
1. **Audio Extraction**: Uses FFmpeg to extract the audio stream into a 16kHz mono WAV file.
2. **Transcription**: Processes the audio through `faster-whisper` to generate timestamped text segments.
3. **Encoding**: Formats segments into the SubRip Subtitle (SRT) standard.
Generates subtitles from video files

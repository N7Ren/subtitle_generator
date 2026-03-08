import argparse
import os
import sys
import logging
from audio_processor import extract_audio
from transcriber import transcribe_audio
from formatter import write_srt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def main():
    parser = argparse.ArgumentParser(description="Generate subtitles from video files.")
    parser.add_argument("input", help="Path to the input video file (mp4, mkv, etc.)")
    parser.add_argument("--model", default="base", help="Whisper model size (tiny, base, small, medium, large)")
    parser.add_argument("--output", help="Path to the output SRT file (defaults to input filename with .srt)")
    parser.add_argument("--keep-audio", action="store_true", help="Keep the extracted audio file")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        logging.error(f"Input file not found: {args.input}")
        sys.exit(1)
        
    input_path = os.path.abspath(args.input)
    output_path = args.output or os.path.splitext(input_path)[0] + ".srt"
    temp_audio = os.path.splitext(input_path)[0] + ".wav"
    
    try:
        # 1. Extract audio
        extract_audio(input_path, temp_audio)
        
        # 2. Transcribe
        segments = transcribe_audio(temp_audio, model_size=args.model)
        
        # 3. Save subtitles
        write_srt(segments, output_path)
        logging.info(f"Subtitles generated successfully: {output_path}")
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)
    finally:
        if not args.keep_audio and os.path.exists(temp_audio):
            os.remove(temp_audio)
            logging.info("Cleaned up temporary audio file.")

if __name__ == "__main__":
    main()

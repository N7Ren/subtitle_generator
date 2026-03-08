import os
import subprocess
import logging

def extract_audio(video_path, audio_path=None):
    """
    Extracts audio from a video file and saves it as a 16kHz mono WAV file.
    
    Args:
        video_path (str): Path to the input video file.
        audio_path (str, optional): Path to save the extracted audio. Defaults to input_filename.wav.
        
    Returns:
        str: The path to the extracted audio file.
    """
    if audio_path is None:
        audio_path = os.path.splitext(video_path)[0] + ".wav"
        
    logging.info(f"Extracting audio from {video_path} to {audio_path}...")
    
    try:
        # ffmpeg -y -i <input> -vn -acodec pcm_s16le -ar 16000 -ac 1 <output>
        command = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            audio_path
        ]
        
        subprocess.run(command, check=True, capture_output=True)
        return audio_path
    except subprocess.CalledProcessError as e:
        logging.error(f"FFmpeg failed: {e.stderr.decode()}")
        raise RuntimeError(f"Failed to extract audio from {video_path}")

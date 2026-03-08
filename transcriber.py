from faster_whisper import WhisperModel
import logging
from tqdm import tqdm

def transcribe_audio(audio_path, model_size="base", device="cpu", compute_type="int8"):
    """
    Transcribes an audio file into segments with timestamps.
    
    Args:
        audio_path (str): Path to the audio file.
        model_size (str): Whisper model size (tiny, base, small, medium, large).
        device (str): Device to run on (cpu, cuda).
        compute_type (str): Model precision (int8, float16, etc).
        
    Returns:
        list: List of transcription segments.
    """
    logging.info(f"Loading Whisper model '{model_size}' on '{device}'...")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    
    logging.info(f"Transcribing {audio_path}...")
    # Using vad_filter=True avoids including leading music/silence in the first segment
    segments, info = model.transcribe(audio_path, beam_size=5, vad_filter=True)
    
    logging.info(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")
    
    result_segments = []
    # Use tqdm if possible, but segments is an iterator
    for segment in segments:
        result_segments.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })
        
    return result_segments

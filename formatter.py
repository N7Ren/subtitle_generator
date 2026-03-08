def format_timestamp(seconds):
    """Formats seconds into SRT timestamp (HH:MM:SS,mmm)."""
    td = float(seconds)
    hours = int(td // 3600)
    minutes = int((td % 3600) // 60)
    secs = int(td % 60)
    millis = int((td % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def to_srt(segments):
    """Converts segments to SRT format string."""
    lines = []
    for i, segment in enumerate(segments, 1):
        start = format_timestamp(segment["start"])
        end = format_timestamp(segment["end"])
        text = segment["text"]
        
        lines.append(str(i))
        lines.append(f"{start} --> {end}")
        lines.append(text)
        lines.append("") # Empty line between entries
        
    return "\n".join(lines)

def write_srt(segments, output_path):
    """Writes segments to an SRT file."""
    content = to_srt(segments)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    return output_path

def preprocess_transcript(transcript: list) -> str:
    return " ".join(turn["text"].strip() for turn in transcript)

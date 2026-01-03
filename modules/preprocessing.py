def preprocess_transcript(transcript: list) -> str:
    """
    Combine transcript turns into a single clean text string.
    """

    return " ".join(turn["text"].strip() for turn in transcript)

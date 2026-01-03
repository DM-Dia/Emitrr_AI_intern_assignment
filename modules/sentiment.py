from transformers import pipeline

# Pretrained lightweight sentiment model
_sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_sentiment_and_intent(text: str) -> dict:
    """
    Analyze patient sentiment and intent from text.
    """

    result = _sentiment_model(text)[0]

    lowered = text.lower()

    if "anxious" in lowered or "worried" in lowered:
        sentiment = "Anxious"
        intent = "Seeking reassurance"
    elif "pain" in lowered:
        sentiment = "Neutral"
        intent = "Reporting symptoms"
    else:
        sentiment = "Reassured"
        intent = "General follow-up"

    return {
        "Sentiment": sentiment,
        "Intent": intent
    }
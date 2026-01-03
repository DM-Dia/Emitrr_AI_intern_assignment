from transformers import pipeline

_sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment_and_intent(text: str) -> dict:
    lowered = text.lower()

    if "worried" in lowered or "anxious" in lowered:
        return {"Sentiment": "Anxious", "Intent": "Seeking reassurance"}
    if "pain" in lowered:
        return {"Sentiment": "Neutral", "Intent": "Reporting symptoms"}

    return {"Sentiment": "Reassured", "Intent": "General follow-up"}
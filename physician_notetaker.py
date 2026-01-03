import json

from modules.preprocessing import preprocess_transcript
from modules.ner import extract_medical_entities
from modules.keyword_extraction import extract_keywords
from modules.summarization import generate_structured_summary
from modules.sentiment import analyze_sentiment_and_intent
from modules.soap import generate_soap_note


def main():
    with open("data/sample_transcripts.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    for case in cases:
        print("\n==============================")
        print("Conversation ID:", case["conversation_id"])
        print("Patient:", case["patient_name"])

        # Step 1: Preprocess
        text = preprocess_transcript(case["transcript"])

        # Step 2: NLP pipeline
        entities = extract_medical_entities(text)
        keywords = extract_keywords(text)
        summary = generate_structured_summary(
            case["patient_name"], text, entities
        )
        sentiment = analyze_sentiment_and_intent(text)
        soap = generate_soap_note(text, entities)

        # Output
        print("\n--- Extracted Entities ---")
        print(entities)

        print("\n--- Keywords ---")
        print(keywords)

        print("\n--- Structured Summary ---")
        print(summary)

        print("\n--- Sentiment & Intent ---")
        print(sentiment)

        print("\n--- SOAP Note ---")
        print(soap)


if __name__ == "__main__":
    main()
import spacy
from collections import defaultdict

# Load spaCy model 
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError(
        "spaCy model not found. Please install with: python -m spacy download en_core_web_sm"
    )


def extract_medical_entities(text: str) -> dict:
    doc = nlp(text)
    entities = defaultdict(list)

    # Rule-based medical extraction (safe + explainable)
    lowered = text.lower()

    if "neck pain" in lowered:
        entities["Symptoms"].append("Neck pain")
    if "back pain" in lowered or "backache" in lowered:
        entities["Symptoms"].append("Back pain")

    if "whiplash" in lowered:
        entities["Diagnosis"].append("Whiplash injury")

    if "physiotherapy" in lowered:
        entities["Treatment"].append("Physiotherapy")
    if "painkiller" in lowered:
        entities["Treatment"].append("Painkillers")

    # Deduplicate
    for k in entities:
        entities[k] = list(set(entities[k]))

    return dict(entities)
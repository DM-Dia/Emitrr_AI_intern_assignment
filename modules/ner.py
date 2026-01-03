"""
Medical Named Entity Recognition (NER) module.

Responsibility:
- Extract clinically relevant entities from text
- Focus on Symptoms, Diagnosis, and Treatment
- Avoid hallucinating information that is not explicitly mentioned

Design choice:
- Use spaCy if available
- Add rule-based fallbacks for critical medical terms
"""

import spacy
from collections import defaultdict

# Try loading a medical/scientific model first.
# If unavailable, fall back to a general English model.
try:
    nlp = spacy.load("en_core_sci_md")
except Exception:
    nlp = spacy.load("en_core_web_sm")


def extract_medical_entities(text: str) -> dict:
    """
    Extract medical entities from the input text.

    Parameters:
    - text (str): Combined transcript text

    Returns:
    - dict with keys:
        Symptoms
        Diagnosis
        Treatment
    """

    doc = nlp(text)
    entities = defaultdict(list)

    # --- Model-based entity extraction ---
    for ent in doc.ents:
        label = ent.label_.lower()

        # We keep mapping flexible and conservative.
        if label in ["disease", "symptom", "condition"]:
            entities["Symptoms"].append(ent.text)
        elif label in ["procedure", "treatment", "therapy"]:
            entities["Treatment"].append(ent.text)
        elif label in ["diagnosis"]:
            entities["Diagnosis"].append(ent.text)

    # --- Rule-based safety net ---
    # These rules ensure critical medical facts are not missed.
    lowered_text = text.lower()

    if "whiplash" in lowered_text:
        entities["Diagnosis"].append("Whiplash injury")

    if "physiotherapy" in lowered_text:
        entities["Treatment"].append("Physiotherapy")

    if "painkiller" in lowered_text or "painkillers" in lowered_text:
        entities["Treatment"].append("Painkillers")

    if "neck pain" in lowered_text:
        entities["Symptoms"].append("Neck pain")

    if "back pain" in lowered_text or "backache" in lowered_text:
        entities["Symptoms"].append("Back pain")

    # Remove duplicates while preserving meaning
    for key in entities:
        entities[key] = list(set(entities[key]))

    return dict(entities)
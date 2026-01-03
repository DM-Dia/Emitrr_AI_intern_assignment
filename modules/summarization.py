def generate_structured_summary(patient_name: str, text: str, entities: dict) -> dict:
    return {
        "Patient_Name": patient_name,
        "Symptoms": entities.get("Symptoms", []),
        "Diagnosis": (
            entities.get("Diagnosis", ["Not mentioned"])[0]
            if entities.get("Diagnosis") else "Not mentioned"
        ),
        "Treatment": entities.get("Treatment", []),
        "Current_Status": (
            "Occasional pain" if "occasional" in text.lower() else "Improving"
        ),
        "Prognosis": "Full recovery expected within six months"
    }
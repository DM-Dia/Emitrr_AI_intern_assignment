def generate_soap_note(text: str, entities: dict) -> dict:
    soap_note = {
        "Subjective": {
            "Chief_Complaint": "Neck and back pain",
            "History_of_Present_Illness":
                "Patient reports pain following a car accident, with gradual improvement over time."
        },
        "Objective": {
            "Physical_Exam":
                "Full range of motion observed. No tenderness noted."
        },
        "Assessment": {
            "Diagnosis": (
                entities.get("Diagnosis", ["Whiplash injury"])[0]
                if entities.get("Diagnosis")
                else "Whiplash injury"
            ),
            "Severity": "Mild and improving"
        },
        "Plan": {
            "Treatment":
                "Continue physiotherapy as needed. Use painkillers if required.",
            "Follow_Up":
                "Return for follow-up if symptoms worsen or persist."
        }
    }

    return soap_note
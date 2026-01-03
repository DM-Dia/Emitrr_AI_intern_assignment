# Design Notes – Physician Notetaker

This document explains the **design decisions, model choices, and reasoning** behind the Physician Notetaker system.
Each section corresponds directly to the questions asked in the assignment.

---

## 1. Medical NLP Summarization

### Q1. How would you handle ambiguous or missing medical data in the transcript?

Medical conversations often contain incomplete or ambiguous information. In this system, ambiguity is handled by:

* Extracting only explicitly stated medical facts
* Using safe default values such as `"Not mentioned"` when a diagnosis or treatment is unclear
* Avoiding inference or hallucination of symptoms or conditions
* Structuring outputs so that missing fields are still present but clearly labeled

This approach prioritizes **clinical safety and explainability**, which is essential in healthcare applications.

---

### Q2. What pre-trained NLP models would you use for medical summarization?

For this assignment, a lightweight and explainable approach was chosen. In a production-grade system, the following models would be appropriate:

* **spaCy / SciSpaCy** for medical entity recognition
* **ClinicalBERT / BioBERT** for understanding clinical context
* **T5 or PEGASUS** fine-tuned on medical summarization datasets for abstractive summaries

In this implementation, rule-based extraction combined with general NLP models was preferred to keep the system transparent and easy to evaluate.

---

## 2. Sentiment & Intent Analysis

### Q3. How would you fine-tune BERT for medical sentiment detection?

Fine-tuning BERT for healthcare sentiment analysis would involve:

1. Collecting labeled medical conversation data
2. Defining sentiment labels such as *Anxious*, *Neutral*, and *Reassured*
3. Fine-tuning a pre-trained model like **ClinicalBERT** on this dataset
4. Validating performance using precision, recall, and F1-score

For this assignment, a **pre-trained DistilBERT model** was used to demonstrate transformer-based sentiment analysis without additional training complexity.

---

### Q4. What datasets would you use for training a healthcare-specific sentiment model?

Relevant datasets include:

* MIMIC-III / MIMIC-IV clinical notes
* i2b2 clinical NLP challenge datasets
* Synthetic or anonymized doctor-patient conversations
* Public health forum or patient feedback datasets

All datasets must be handled with strict privacy and ethical considerations.

---

## 3. SOAP Note Generation

### Q5. How would you train an NLP model to map transcripts into SOAP format?

Mapping transcripts to SOAP format can be approached in two ways:

* **Rule-based mapping** using section-specific heuristics
* **Sequence-to-sequence models** trained on transcript–SOAP pairs

A hybrid approach is often most effective, where rules ensure structural correctness and ML models handle language variability.

For this assignment, a rule-based approach was chosen for clarity and reliability.

---

### Q6. What rule-based or deep-learning techniques would improve SOAP note accuracy?

Potential improvements include:

* Named entity alignment with SOAP sections
* Contextual embeddings to distinguish subjective vs objective statements
* Fine-tuned transformer models for SOAP generation
* Post-processing validation rules to ensure clinical consistency

Such techniques would improve accuracy while maintaining interpretability.

---

## 4. Design Trade-offs & Rationale

* **Explainability over complexity**: The system favors simple, interpretable logic
* **Safety over inference**: No assumptions beyond explicit text
* **Modularity**: Each NLP task is implemented as a separate module
* **Scalability**: The pipeline supports multiple conversations with no code changes

These trade-offs align with real-world healthcare AI requirements.

---

## 5. Limitations & Future Improvements

* Incorporate domain-specific medical language models
* Fine-tune sentiment models on clinical data
* Improve summarization using transformer-based generative models
* Add persistent output storage (database or API integration)
* Integrate speech-to-text for real-time physician dictation

---

## Conclusion

This project demonstrates a **clean, modular, and explainable NLP pipeline** for medical conversation analysis.
The design emphasizes **engineering judgment, safety, and clarity**, which are critical for healthcare-focused AI systems.

---
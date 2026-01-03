# Physician Notetaker – AI Intern Assignment (Emitrr)

## Overview

This project implements an **Physician Notetaker system** that processes transcribed physician–patient conversations and extracts clinically relevant information using Natural Language Processing (NLP).

The system demonstrates:

* Medical entity extraction (Symptoms, Diagnosis, Treatment)
* Structured medical summarization
* Patient sentiment and intent analysis
* Automated SOAP note generation

The focus of this assignment is on **clear problem-solving, sound engineering decisions, and explainable AI design**.

---

## Key Features

* **Medical NLP Pipeline**

  * Rule-based and NLP-assisted extraction of medical entities
  * Safe and conservative handling of clinical information

* **Structured Medical Summary**

  * Converts raw conversation text into a clean JSON medical report

* **Sentiment & Intent Analysis**

  * Uses a transformer-based sentiment model (DistilBERT)
  * Identifies patient intent such as reporting symptoms or seeking reassurance

* **SOAP Note Generation**

  * Automatically structures clinical information into SOAP format
  * Improves clinical readability and documentation consistency

---

## Project Structure

```
physician-notetaker/
│
├── data/
│   └── sample_transcripts.json
│
├── modules/
│   ├── preprocessing.py
│   ├── ner.py
│   ├── keyword_extraction.py
│   ├── summarization.py
│   ├── sentiment.py
│   └── soap.py
│
├── outputs/
│   ├── structured_summary_case_001.json
│   ├── sentiment_intent_case_001.json
│   └── soap_note_case_001.json
│
├── docs/
│   └── design_notes.md
│
├── physician_notetaker.py
├── requirements.txt
└── README.md
```

---

## Assignment Questions & Design Explanations

All **section-wise conceptual questions** asked in the assignment are answered in detail in:

```
docs/design_notes.md
```

This document includes:

* Handling of ambiguous or missing medical data
* Choice of NLP and transformer models
* Approach to medical summarization
* Strategy for sentiment and intent detection
* Design considerations for SOAP note generation
* Discussion of rule-based vs deep-learning approaches

---

## Input Format

Input conversations are provided in JSON format:

```json
{
  "conversation_id": "case_001",
  "patient_name": "Janet Jones",
  "transcript": [
    { "speaker": "Physician", "text": "How are you feeling today?" },
    { "speaker": "Patient", "text": "I still have some neck and back pain." }
  ]
}
```

The system supports **multiple conversations** in a single input file.

---

## Output Examples

The `outputs/` directory contains **representative sample outputs** for one conversation to illustrate the expected JSON schema:

* Structured medical summary
* Sentiment & intent classification
* SOAP note

> Note: Only one representative case is saved as output files to keep the repository clean.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd physician-notetaker
```

### 2. Create & Activate Virtual Environment 

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

---

## How to Run

Run the full NLP pipeline using:

```bash
python physician_notetaker.py
```

The script:

1. Loads sample conversations
2. Preprocesses text
3. Extracts medical entities
4. Generates structured summaries
5. Performs sentiment & intent analysis
6. Produces SOAP notes

---

## Design Philosophy

* **Explainability over complexity**
  Emphasis on interpretable logic and safe defaults.

* **Healthcare-aware conservatism**
  No assumptions beyond explicitly stated information.

* **Modular engineering**
  Each NLP task is implemented as an independent module.

---

## Limitations & Future Improvements

* Use domain-specific medical NER models (e.g., SciSpaCy)
* Fine-tune sentiment models on healthcare datasets
* Improve SOAP accuracy using sequence-to-sequence models
* Add persistent output storage
* Integrate speech-to-text for real-time use

---

## Notes

* This project is intended as a **technical assignment demonstration**, not a clinical system.
* No real patient data (PHI) is used.

---

## Author

**Devansi Mahatar**
Computer Science & Engineering
AI / Data Science Enthusiast

---
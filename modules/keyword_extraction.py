"""
Keyword Extraction Module

Responsibility:
- Identify important words and short phrases from medical conversations
- Support summarization and downstream analysis

"""

from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text: str, top_k: int = 10) -> list:
    
    # TF-IDF considers term importance relative to the document
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),  # unigrams + bigrams
        max_features=top_k
    )

    tfidf_matrix = vectorizer.fit_transform([text])

    # Get feature names 
    keywords = vectorizer.get_feature_names_out()

    return keywords.tolist()

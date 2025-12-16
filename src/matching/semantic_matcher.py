from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def semantic_similarity(resume_text: str, jd_text: str) -> float:
    """
    Compute semantic similarity between resume and JD
    """
    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    return round(float(similarity), 3)

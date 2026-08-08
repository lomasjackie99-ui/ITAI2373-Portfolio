from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSearchEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.documents = []
        self.document_vectors = None

    def index_documents(self, documents):
        """Store documents and create searchable vectors."""
        self.documents = documents
        self.document_vectors = self.vectorizer.fit_transform(documents)

    def search(self, query, top_k=3):
        """Find the documents most similar to a query."""
        if self.document_vectors is None:
            return []

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.document_vectors
        )[0]

        top_indexes = scores.argsort()[::-1][:top_k]

        results = []

        for index in top_indexes:
            results.append({
                "article": self.documents[index],
                "score": float(scores[index])
            })

        return results

    def compare_articles(self, article1, article2):
        """Measure similarity between two articles."""
        vectors = self.vectorizer.fit_transform(
            [article1, article2]
        )

        return float(
            cosine_similarity(vectors[0], vectors[1])[0][0]
        )
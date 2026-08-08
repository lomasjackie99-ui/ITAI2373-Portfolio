from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class NewsClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words="english"
        )
        self.model = MultinomialNB()

    def train(self, texts, labels):
        """Train the news classification model."""
        features = self.vectorizer.fit_transform(texts)
        self.model.fit(features, labels)

    def predict(self, text):
        """Predict the category of a news article."""
        features = self.vectorizer.transform([text])
        return self.model.predict(features)[0]

    def predict_with_confidence(self, text):
        """Predict a category and return its confidence score."""
        features = self.vectorizer.transform([text])

        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]

        confidence = max(probabilities)

        return {
            "category": prediction,
            "confidence": float(confidence)
        }
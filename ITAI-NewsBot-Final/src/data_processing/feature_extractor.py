from sklearn.feature_extraction.text import TfidfVectorizer

class FeatureExtractor:
    def __init__(self, max_features=5000):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            stop_words="english"
        )

    def fit_transform(self, documents):
        """Learn vocabulary and create TF-IDF features."""
        return self.vectorizer.fit_transform(documents)

    def transform(self, documents):
        """Create TF-IDF features for new documents."""
        return self.vectorizer.transform(documents)

    def get_feature_names(self):
        """Return the words used as TF-IDF features."""
        return self.vectorizer.get_feature_names_out()
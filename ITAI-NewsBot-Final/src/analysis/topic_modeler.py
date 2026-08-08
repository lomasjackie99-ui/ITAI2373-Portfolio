from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation, NMF


class TopicModeler:
    def __init__(self, n_topics=5, method="lda"):
        self.n_topics = n_topics
        self.method = method.lower()

        self.vectorizer = CountVectorizer(
            max_features=1000,
            stop_words="english"
        )

        if self.method == "nmf":
            self.model = NMF(
                n_components=n_topics,
                random_state=42
            )
        else:
            self.model = LatentDirichletAllocation(
                n_components=n_topics,
                random_state=42
            )

    def fit_transform(self, documents):
        """Train the topic model and transform documents."""
        features = self.vectorizer.fit_transform(documents)
        return self.model.fit_transform(features)

    def get_topic_words(self, topic_id, n_words=10):
        """Return the most important words for a topic."""
        feature_names = self.vectorizer.get_feature_names_out()

        topic = self.model.components_[topic_id]

        top_indexes = topic.argsort()[-n_words:][::-1]

        return [feature_names[index] for index in top_indexes]

    def get_all_topics(self, n_words=10):
        """Return keywords for every discovered topic."""
        topics = {}

        for topic_id in range(self.n_topics):
            topics[f"Topic {topic_id + 1}"] = self.get_topic_words(
                topic_id,
                n_words
            )

        return topics
from textblob import TextBlob


class SentimentAnalyzer:
    def analyze(self, text):
        """Analyze whether text is positive, negative, or neutral."""
        polarity = TextBlob(str(text)).sentiment.polarity

        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            "sentiment": sentiment,
            "score": polarity
        }

    def analyze_articles(self, articles):
        """Analyze sentiment for multiple articles."""
        results = []

        for article in articles:
            results.append(self.analyze(article))

        return results
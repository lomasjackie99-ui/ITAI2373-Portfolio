import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt", quiet=True)


class IntelligentSummarizer:
    def summarize(self, text, max_sentences=3):
        """Create a simple extractive summary."""
        if text is None or len(str(text).strip()) == 0:
            return ""

        sentences = sent_tokenize(str(text))

        if len(sentences) <= max_sentences:
            return str(text).strip()

        return " ".join(sentences[:max_sentences])

    def summarize_multiple(self, articles, max_sentences=3):
        """Summarize multiple articles."""
        summaries = []

        for article in articles:
            summaries.append(
                self.summarize(article, max_sentences=max_sentences)
            )

        return summaries
from src.data_processing.text_preprocessor import TextPreprocessor
from src.analysis.sentiment_analyzer import SentimentAnalyzer


def test_system_integration():
    processor = TextPreprocessor()
    sentiment = SentimentAnalyzer()

    article = "The company announced excellent results and strong growth."

    cleaned_article = processor.preprocess(article)
    result = sentiment.analyze(cleaned_article)

    assert cleaned_article != ""
    assert "sentiment" in result
    assert "score" in result
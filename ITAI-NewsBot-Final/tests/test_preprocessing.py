from src.data_processing.text_preprocessor import TextPreprocessor


def test_preprocessing():
    processor = TextPreprocessor()

    result = processor.preprocess(
        "The NewsBot is analyzing NEWS articles!"
    )

    assert isinstance(result, str)
    assert len(result) > 0
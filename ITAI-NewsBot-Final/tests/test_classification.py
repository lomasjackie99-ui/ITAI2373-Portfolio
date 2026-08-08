from src.analysis.classifier import NewsClassifier


def test_classification():
    classifier = NewsClassifier()

    texts = [
        "The basketball team won the championship.",
        "A new artificial intelligence system was released."
    ]

    labels = ["sports", "technology"]

    classifier.train(texts, labels)

    prediction = classifier.predict(
        "The team won another basketball game."
    )

    assert prediction in labels
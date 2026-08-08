from src.analysis.topic_modeler import TopicModeler


def test_topic_modeling():
    documents = [
        "Artificial intelligence is changing technology.",
        "Machine learning is used in many AI systems.",
        "The basketball team won the game.",
        "Sports teams are preparing for the season."
    ]

    modeler = TopicModeler(n_topics=2)

    results = modeler.fit_transform(documents)

    assert results.shape[0] == len(documents)
    assert results.shape[1] == 2
import matplotlib.pyplot as plt


def plot_topic_scores(topic_names, scores):
    """Create a simple bar chart for topic scores."""
    plt.figure(figsize=(8, 5))
    plt.bar(topic_names, scores)
    plt.title("Topic Modeling Results")
    plt.xlabel("Topics")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_test_results(passed, failed):
    """Create a simple chart showing passed and failed tests."""
    labels = ["Passed", "Failed"]
    values = [passed, failed]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title("NewsBot Test Results")
    plt.ylabel("Number of Tests")
    plt.tight_layout()
    plt.show()
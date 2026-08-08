class IntentClassifier:
    def classify_intent(self, query):
        """Identify what the user is asking NewsBot to do."""
        query = str(query).lower()

        if "summary" in query or "summarize" in query:
            return "summarization"
        elif "sentiment" in query or "positive" in query or "negative" in query:
            return "sentiment"
        elif "translate" in query or "translation" in query:
            return "translation"
        elif "topic" in query:
            return "topic"
        elif "similar" in query or "search" in query:
            return "search"
        elif "entity" in query or "person" in query or "organization" in query:
            return "entities"
        else:
            return "general"
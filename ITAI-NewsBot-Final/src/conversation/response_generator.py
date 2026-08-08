class ResponseGenerator:
    def generate_response(self, intent, results=None):
        """Create a simple response based on user intent."""
        if results is None:
            results = {}

        if intent == "summarization":
            return results.get(
                "summary",
                "I could not create a summary."
            )

        if intent == "sentiment":
            return (
                f"The article sentiment is "
                f"{results.get('sentiment', 'unknown')}."
            )

        if intent == "translation":
            return results.get(
                "translation",
                "Translation is not available."
            )

        if intent == "topic":
            return str(results.get("topics", "No topics found."))

        if intent == "search":
            return str(results.get("search_results", "No results found."))

        if intent == "entities":
            return str(results.get("entities", "No entities found."))

        return "I can help analyze, summarize, translate, or search news."
class QueryProcessor:
    def __init__(self, intent_classifier=None):
        self.intent_classifier = intent_classifier

    def process_query(self, query):
        """Process a user question and identify its intent."""
        if query is None or len(str(query).strip()) == 0:
            return {
                "query": "",
                "intent": "invalid",
                "message": "Please enter a question."
            }

        intent = "general"

        if self.intent_classifier is not None:
            intent = self.intent_classifier.classify_intent(query)

        return {
            "query": str(query).strip(),
            "intent": intent
        }
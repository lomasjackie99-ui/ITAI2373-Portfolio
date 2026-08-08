class DataValidator:
    def validate_text(self, text):
        """Check that the text is usable."""
        if text is None:
            return False

        text = str(text).strip()

        if len(text) == 0:
            return False

        return True

    def validate_documents(self, documents):
        """Remove empty or invalid documents."""
        valid_documents = []

        for document in documents:
            if self.validate_text(document):
                valid_documents.append(str(document).strip())

        return valid_documents
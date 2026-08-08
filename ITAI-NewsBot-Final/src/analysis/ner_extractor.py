import spacy


class EntityExtractor:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            self.nlp = None
            print(
                "spaCy English model not found. "
                "Run: python -m spacy download en_core_web_sm"
            )

    def extract_entities(self, text):
        """Find important people, places, organizations, and other entities."""
        if self.nlp is None:
            return []

        doc = self.nlp(str(text))

        entities = []

        for entity in doc.ents:
            entities.append({
                "text": entity.text,
                "label": entity.label_
            })

        return entities
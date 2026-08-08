from transformers import MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-es-en"

        try:
            self.tokenizer = MarianTokenizer.from_pretrained(
                self.model_name
            )
            self.model = MarianMTModel.from_pretrained(
                self.model_name
            )
        except Exception:
            self.tokenizer = None
            self.model = None

    def translate_spanish_to_english(self, text):
        """Translate Spanish text into English."""
        if self.tokenizer is None or self.model is None:
            return "Translation model is not available."

        inputs = self.tokenizer(
            str(text),
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        translated = self.model.generate(**inputs)

        return self.tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )
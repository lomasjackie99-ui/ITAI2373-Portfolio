from langdetect import detect


class LanguageDetector:
    def detect_language(self, text):
        """Detect the language of the text."""
        try:
            return detect(str(text))
        except Exception:
            return "unknown"
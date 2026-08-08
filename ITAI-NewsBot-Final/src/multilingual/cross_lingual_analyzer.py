class CrossLingualAnalyzer:
    def compare_texts(self, original_text, translated_text):
        """Create a simple comparison between two language versions."""
        return {
            "original_length": len(str(original_text).split()),
            "translated_length": len(str(translated_text).split()),
            "original_text": str(original_text),
            "translated_text": str(translated_text)
        }

    def create_comparison_summary(self, original_text, translated_text):
        """Explain the basic cross-language comparison."""
        comparison = self.compare_texts(
            original_text,
            translated_text
        )

        return (
            f"Original text has "
            f"{comparison['original_length']} words and the "
            f"translated text has "
            f"{comparison['translated_length']} words."
        )
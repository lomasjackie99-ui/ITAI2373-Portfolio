import json


class ResultExporter:
    def export_json(self, results, filename):
        """Save NewsBot results as a JSON file."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4, ensure_ascii=False)

        return filename

    def export_text(self, text, filename):
        """Save NewsBot output as a text file."""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(text))

        return filename
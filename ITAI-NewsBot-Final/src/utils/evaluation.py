class EvaluationHelper:
    def calculate_accuracy(self, correct, total):
        """Calculate a simple accuracy percentage."""
        if total == 0:
            return 0.0

        return (correct / total) * 100

    def summarize_tests(self, passed, failed):
        """Return a summary of system test results."""
        total = passed + failed

        return {
            "total_tests": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": self.calculate_accuracy(passed, total)
        }
class ErrorHandler:
    def __init__(self):
        self.errors = []

    def report(self, message):
        self.errors.append(message)

    def has_errors(self):
        return len(self.errors) > 0

    def display_errors(self):
        for error in self.errors:
            print("Error:", error)

class NullReferenceException(Exception):
    def __init__(self, message="Missing pet information."):
        self.message = message
        super().__init__(self.message)

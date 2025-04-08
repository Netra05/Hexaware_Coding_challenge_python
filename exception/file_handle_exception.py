class FileHandlingException(Exception):
    def __init__(self, message="Error while accessing file."):
        self.message = message
        super().__init__(self.message)

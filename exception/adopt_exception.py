class AdoptionException(Exception):
    def __init__(self, message="Something went wrong during adoption"):
        self.message = message
        super().__init__(self.message)

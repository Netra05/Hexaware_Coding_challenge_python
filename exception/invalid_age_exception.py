# exception/invalid_age_exception.py

class InvalidAgeException(Exception):
    def __init__(self, message="Invalid age. Age must be a positive number."):
        super().__init__(message)

# dao/donation.py
from abc import ABC, abstractmethod

class Donation(ABC):
    def __init__(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount

    def get_donor_name(self):
        return self.donor_name

    def get_amount(self):
        return self.amount

    def set_donor_name(self, donor_name):
        self.donor_name = donor_name

    def set_amount(self, amount):
        self.amount = amount

    @abstractmethod
    def record_donation(self, conn):
        pass

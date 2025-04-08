# dao/cash_donation.py

from dao.donation import Donation
from datetime import datetime

class CashDonation(Donation):
    def __init__(self, donor_name, amount):
        super().__init__(donor_name, amount)
        self.donation_date = datetime.now()

    def record_donation(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donations (donor_name, amount, donation_type, donation_date)
                VALUES (?, ?, ?, ?)
            """, (self.donor_name, self.amount, "Cash", self.donation_date))
            conn.commit()
            print("Cash donation recorded.")
        except Exception as e:
            print("Error recording donation:", e)

# dao/item_donation.py

from dao.donation import Donation

class ItemDonation(Donation):
    def __init__(self, donor_name, amount, item_type):
        super().__init__(donor_name, amount)
        self.item_type = item_type

    def record_donation(self, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donations (donor_name, amount, donation_type, item_type)
                VALUES (?, ?, ?, ?)
            """, (self.donor_name, self.amount, "Item", self.item_type))
            conn.commit()
            print("Item donation recorded.")
        except Exception as e:
            print("Error recording donation:", e)

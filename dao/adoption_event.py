# dao/adoption_event.py

from util.db_conn_util import get_connection
from dao.iadoptable import IAdoptable

class AdoptionEvent(IAdoptable):
    def __init__(self):
        self.participants = []

    def adopt(self):
        # Dummy method to satisfy the interface
        pass

    def register_participant(self, name):
        self.participants.append(name)
        print(f"{name} registered for the event.")

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Get the most recent event ID
            cursor.execute("SELECT TOP 1 event_id FROM adoption_events ORDER BY event_id DESC")
            row = cursor.fetchone()

            if row:
                event_id = row[0]
                cursor.execute("INSERT INTO participants (name, event_id) VALUES (?, ?)", (name, event_id))
                conn.commit()
                print(f"{name} successfully added to participants for event ID {event_id}")
            else:
                print("No adoption event found. Please add an event first.")

        except Exception as e:
            print("Error while adding participant:", e)

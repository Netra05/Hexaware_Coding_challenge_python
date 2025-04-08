import datetime
from util.db_conn_util import get_connection
from entity.dog import Dog
from entity.cat import Cat
from entity.pet_shelter import PetShelter
from dao.cash_donation import CashDonation
from dao.item_donation import ItemDonation
from dao.adoption_event import AdoptionEvent
from exception.invalid_age_exception import InvalidAgeException
from exception.null_ref_exception import NullReferenceException
from exception.insuff_fund_exception import InsufficientFundsException
from exception.adopt_exception import AdoptionException

def main():
    conn = get_connection()
    shelter = PetShelter()
    event = AdoptionEvent()

    while True:
        print("\n======= PetPals Platform =======")
        print("1. Add Pet")
        print("2. List All Pets")
        print("3. Make a Cash Donation")
        print("4. Make an Item Donation")
        print("5. Register for Adoption Event")
        print("6. View All Donations")
        print("7. List Adoption Events")
        print("8. Add Adoption Event")
        print("9.View Registered Participants")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pet_type = input("Is it a Dog or Cat? ").strip().lower()
            name = input("Enter pet name: ")
            try:
                age = int(input("Enter pet age: "))
                if age <= 0:
                    raise InvalidAgeException()
                breed = input("Enter breed: ")

                if pet_type == "dog":
                    dog_breed = input("Enter dog breed: ")
                    pet = Dog(name, age, breed, dog_breed)
                elif pet_type == "cat":
                    cat_color = input("Enter cat color: ")
                    pet = Cat(name, age, breed, cat_color)
                else:
                    print("Invalid pet type.")
                    continue

                shelter.add_pet(pet, conn)

            except InvalidAgeException as e:
                print(e)
            except ValueError:
                print("Age must be an integer.")

        elif choice == '2':
            try:
                shelter.list_available_pets()
            except NullReferenceException as e:
                print(e)

        elif choice == '3':
            name = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation amount: "))
                if amount < 10:
                    raise InsufficientFundsException()
                donation = CashDonation(name, amount)
                donation.record_donation(conn)
            except InsufficientFundsException as e:
                print(e)
            except ValueError:
                print("Amount must be a number.")

        elif choice == '4':
            name = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation value (est.): "))
                item_type = input("Enter item type: ")
                donation = ItemDonation(name, amount, item_type)
                donation.record_donation(conn)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            participant_name = input("Enter your name to register: ")
            try:
                if not participant_name.strip():
                    raise AdoptionException("Name cannot be empty.")
                event.register_participant(participant_name)
            except AdoptionException as e:
                print(e)

        elif choice == '6':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM donations")
                donations = cursor.fetchall()
                if not donations:
                    print("No donations available.")
                else:
                    print("\n--- Donations ---")
                    for d in donations:
                        print(f"Donor: {d.donor_name}, Amount: {d.amount}, Type: {d.donation_type}, Date: {d.donation_date}, Item: {d.item_type}")
            except Exception as e:
                print("Error fetching donations:", e)

        elif choice == '7':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM adoption_events")
                events = cursor.fetchall()
                if not events:
                    print("No adoption events scheduled.")
                else:
                    print("\n--- Adoption Events ---")
                    for e in events:
                        print(f"Event ID: {e.event_id}, Name: {e.event_name}, Date: {e.event_date}")
            except Exception as e:
                print("Error listing events:", e)

        elif choice == '8':
            try:
                event_name = input("Enter event name: ")
                event_date_input = input("Enter event date (YYYY-MM-DD): ")
                event_date = datetime.datetime.strptime(event_date_input, '%Y-%m-%d').date()

                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO adoption_events (event_name, event_date) 
                    VALUES (?, ?)
                """, (event_name, event_date))
                conn.commit()
                print("Adoption event added successfully.")
            except Exception as e:
                print("Error adding event:", e)

        elif choice == '10':
            print("Closing the app. Take care!")
            break

        elif choice == '9':
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.participant_id, p.name, a.event_name, a.event_date
                    FROM participants p
                    JOIN adoption_events a ON p.event_id = a.event_id
                """)
                participants = cursor.fetchall()
                if not participants:
                    print("No participants registered yet.")
                else:
                    print("\n--- Registered Participants ---")
                    for p in participants:
                        print(f"ID: {p.participant_id}, Name: {p.name}, Event: {p.event_name}, Date: {p.event_date}")
            except Exception as e:
                print("Error fetching participants:", e)


        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

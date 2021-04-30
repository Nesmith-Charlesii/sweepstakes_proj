import random


class Contestant:
    def __init__(self):
        self.first_name = str
        self.last_name = str
        self.email_address = str
        self.registration_number = int

        # prompt user for contestant info
        print("\ncontestant info:")
        self.first_name = input("\tFirst Name: ")
        self.last_name = input("\tLast Name: ")
        self.email_address = input("\tEmail Address: ")
        rand = random.randrange(1, 100)
        self.registration_number = rand
        print(
            f"contestant info confirmation:\n\tfirst name: {self.first_name}\n\tlast name: {self.last_name}\n\temail address: {self.email_address}\n\tregistration number: {self.registration_number}")

    def notify(self, is_winner):
        print(f"Congratulations {is_winner.first_name} {is_winner.last_name}!")

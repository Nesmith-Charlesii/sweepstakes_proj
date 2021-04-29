from contestant import Contestant


class Sweepstake:
    def __init__(self):
        self.name = input("\nwhat is the name of this sweepstake?: ")
        self.contestant_list = []

    def register_contestant(self, contestant):
        contestant_dictionary = {"first name": contestant.first_name,
                                 "last name": contestant.last_name,
                                 "email": contestant.email_address,
                                 "registration number": contestant.registration_number}

        self.contestant_list.append(contestant_dictionary)

    def pick_winner(self):
        

    def print_contestant_info(self, contestant):
        print(
            f"contestant info:\n\tfirst name: {contestant.first_name}\nlast name: {contestant.last_name}\nemail: {contestant.email_address}\nregistration number: {contestant.registration_number}")

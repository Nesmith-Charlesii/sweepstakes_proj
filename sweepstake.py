from contestant import Contestant
import random


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

        rand = random.randrange(0, len(self.contestant_list))
        for val in self.contestant_list:
            if contestant_dictionary['registration number'] == val['registration number']:
                contestant_dictionary["registration number"] = rand

    def pick_winner(self):
        rand = random.randrange(0, len(self.contestant_list))
        winner = self.contestant_list[rand]

        print(f"\nSweepstake winner: {winner['first name']} {winner['last name']}\n")
        # return f"\nSweepstake winner: {winner['first name']} {winner['last name']}"

    def print_contestant_info(self, contestant):
        print(
            f"contestant info:\n\tfirst name: {contestant.first_name}\n\tlast name: {contestant.last_name}\n\temail: {contestant.email_address}\n\tregistration number: {contestant.registration_number}")

    def print_contestant_list(self):
        print(f"\nContestants in sweepstake:\n\t{self.contestant_list}")

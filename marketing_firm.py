from sweepstake import Sweepstake


class Marketing_firm:
    def __init__(self, manager_type):
        self.manager_first_name = input("\nmanager first name: ")
        self.manager_last_name = input("manager last name: ")

        print(f"marketing manager: {self.manager_first_name} {self.manager_last_name}")

    def create_sweepstakes(self):
        return Sweepstake()

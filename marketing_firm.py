from sweepstake import Sweepstake


class Marketing_firm:
    # __init__ method uses dependency injection to utilize a sweepstakes manager instantiated in the marketing_firm_creator class. dependency injection makes access to a sweepstakes manager class easy by using the marketing_firm object attribute 'self.manager' to access methods in the sweepstake manager class
    def __init__(self, manager):
        self.manager_first_name = input("\nmanager first name: ")
        self.manager_last_name = input("manager last name: ")
        self.manager = manager

        print(f"marketing manager: {self.manager_first_name} {self.manager_last_name}")

    def create_sweepstakes(self):
        return Sweepstake()

from sweepstake import Sweepstake
from sweepstakes_queue_manager import Sweepstake_queue_manager
from sweepstakes_stack_manager import Sweepstakes_stack_manager


class Marketing_firm:
    def __init__(self):
        self.manager_first_name = input("\nmanager first name: ")
        self.manager_last_name = input("manager last name: ")
        self.manager_type = None
        print(f"marketing manager: {self.manager_first_name} {self.manager_last_name}")

        manager_type = [Sweepstake_queue_manager(), Sweepstakes_stack_manager()]

        manager_type_choice = input("\nManager type options:\n\t1: queue manager\n\t2: stack manager\nselection: ")
        if manager_type_choice == "1":
            self.manager_type = manager_type[0]
        elif manager_type_choice == "2":
            self.manager_type = manager_type[1]

    def create_sweepstakes(self):
        return Sweepstake()

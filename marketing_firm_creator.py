from marketing_firm import Marketing_firm
from sweepstakes_stack_manager import Sweepstakes_stack_manager
from sweepstakes_queue_manager import Sweepstake_queue_manager


class Marketing_firm_creator:
    @staticmethod
    def choose_manager_type():
        manager_type = [Sweepstake_queue_manager(), Sweepstakes_stack_manager()]
        manager_type_choice = input("\nManager type options:\n\t1: queue manager\n\t2: stack manager\nselection: ")

        if manager_type_choice == "1":
            manager_type = manager_type[0]
            print(f"manager type: {manager_type.name}")
        elif manager_type_choice == "2":
            manager_type = manager_type[1]
            print(f"manager type: {manager_type.name}")

        return Marketing_firm(manager_type)

from contestant import Contestant
from marketing_firm_creator import Marketing_firm_creator


def run_simulation():
    # create marketing_firm_creator object that uses 'choose_manager_type' method to instantiate a market firm
    # 'choose_manager_type' method will prompt user to choose a manager type (queue or stack)
    market_firm = Marketing_firm_creator.choose_manager_type()

    # create 3 sweepstake objects
    sweepstake_1 = market_firm.create_sweepstakes()
    sweepstake_2 = market_firm.create_sweepstakes()
    sweepstake_3 = market_firm.create_sweepstakes()

    # insert each sweepstake object into the "manager" type of the specified market_firm object
    # 3 objects are inserted to demonstrate the queue or stack class methods of inserting or getting a sweepstake
    market_firm.manager.insert_sweepstakes(sweepstake_1.name)
    market_firm.manager.insert_sweepstakes(sweepstake_2.name)
    market_firm.manager.insert_sweepstakes(sweepstake_3.name)

    # create contestant objects
    contestant_1 = Contestant()
    contestant_2 = Contestant()

    # register created contestant objects into specified sweepstake object (sweepstake_1)
    sweepstake_1.register_contestant(contestant_1)
    sweepstake_1.register_contestant(contestant_2)

    # print contestant info of specified contestants
    sweepstake_1.print_contestant_info(contestant_1)
    sweepstake_1.print_contestant_info(contestant_2)

    # display list of dictionaries. each dictionary contains contestant info
    sweepstake_1.print_contestant_list()

    # choose winner at random from the list of dictionaries
    sweepstake_1.pick_winner()

    # demonstrate get (retrieval) of a sweepstakes from either stack or queue
    market_firm.manager.get_sweepstakes()

from contestant import Contestant
from marketing_firm_creator import Marketing_firm_creator


if __name__ == '__main__':
    def run_simulation():
        market_firm_creator = Marketing_firm_creator.choose_manager_type()
        sweepstake = market_firm_creator.create_sweepstakes()
        contestant_1 = Contestant()
        contestant_2 = Contestant()

        sweepstake.register_contestant(contestant_1)
        sweepstake.register_contestant(contestant_2)
        sweepstake.print_contestant_info(contestant_1)
        sweepstake.print_contestant_info(contestant_2)
        sweepstake.print_contestant_list()
        sweepstake.pick_winner()

    run_simulation()

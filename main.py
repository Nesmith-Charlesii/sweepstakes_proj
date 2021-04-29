from contestant import Contestant
from sweepstake import Sweepstake

if __name__ == '__main__':
    def run_simulation():
        contestant_1 = Contestant()
        contestant_2 = Contestant()

        sweepstake = Sweepstake()
        sweepstake.register_contestant(contestant_1)
        sweepstake.register_contestant(contestant_2)

        sweepstake.print_contestant_list()
        sweepstake.pick_winner()
        sweepstake.print_contestant_info(contestant_1)

    run_simulation()

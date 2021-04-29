from contestant import Contestant
from sweepstake import Sweepstake

if __name__ == '__main__':
    def run_simulation():
        contestant_1 = Contestant()
        contestant_2 = Contestant()

        sweepstake = Sweepstake()
        sweepstake.register_contestant(contestant_1)
        sweepstake.register_contestant(contestant_2)

        print(sweepstake.contestant_list)

    run_simulation()

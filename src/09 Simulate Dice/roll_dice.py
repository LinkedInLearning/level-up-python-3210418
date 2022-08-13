from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for roll in range(num_trials):
        counts[sum((randint(1, sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))

if __name__ == '__main__':  # commands from explanation video
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)

from random import randint
from collections import Counter

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1, sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice) + 1):
        print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')


# commands used in solution video for reference
if __name__ == '__main__':
    roll_dice(4, 6, 6)
    roll_dice(4, 6, 6, 20)

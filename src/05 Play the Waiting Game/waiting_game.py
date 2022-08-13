import time
import random

def waiting_game():
    target = random.randint(2, 4)  # target seconds to wait
    print('\nYour target time is {} seconds'.format(target))

    input(' ---Press Enter to Begin--- ')
    start = time.perf_counter()

    input('\n...Press Enter again after {} seconds...'.format(target))
    elapsed = time.perf_counter() - start

    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print('({0:.3f} seconds too fast)'.format(target - elapsed))
    else:
        print('({0:.3f} seconds too slow)'.format(elapsed - target))

# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()

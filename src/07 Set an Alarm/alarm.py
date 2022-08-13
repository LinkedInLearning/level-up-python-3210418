import sched
import time

def countdown(end_time, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(end_time - 3, 1, print, argument=('3...',))
    s.enterabs(end_time - 2, 1, print, argument=('2...',))
    s.enterabs(end_time - 1, 1, print, argument=('1...',))
    s.enterabs(end_time, 1, print, argument=(message,))
    print('Alarm set for', time.asctime(time.localtime(end_time)))
    s.run()


# commands used in solution video for reference
if __name__ == '__main__':
    countdown(time.time()+5, 'Blast Off!')

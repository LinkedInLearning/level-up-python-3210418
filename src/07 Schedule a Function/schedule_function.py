import sched
import time

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()


# commands used in solution video for reference
if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')

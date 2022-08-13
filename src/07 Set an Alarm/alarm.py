import sched
import time
import os

def set_alarm(alarm_time, wav_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, os.system, argument=(f'mpg123 {wav_file}',))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    s.run()

# commands used in solution video for reference
if __name__ == '__main__':
    set_alarm(time.time()+1, 'alarm.wav', 'Wake up!')
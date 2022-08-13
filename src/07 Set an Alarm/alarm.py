import sched
import time
import winsound as ws

def set_alarm(alarm_time, wav_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarm_time)))
    s.run()

if __name__ == '__main__': # commands from explanation video
    set_alarm(time.time()+1, 'alarm.wav', 'Wake up!')
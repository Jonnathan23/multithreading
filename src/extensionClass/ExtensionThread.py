import time
import os
from threading import Thread


class MyThreadClass (Thread):
    def __init__(self, name:str, duration:int):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    
    def run(self):
        print(f"--> {self.name} \n running, belongin to process ID: {str(os.getpid())} \n")
        time.sleep(self.duration)
        print(f"   {self.name} over <--\n")
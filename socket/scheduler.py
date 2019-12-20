import time
from multiprocessing import Queue
import apiAgent

class agentScheduler():
    def __init__(self,schedulingCycle,queue,target = None,args = ()):
        self.schedulingCycle = schedulingCycle
        self.target = target
        self.args = args
        self.queue = queue
        
    def scheduling(self):
        while True:
            time.sleep(self.schedulingCycle)
            self.queue.put(int(time.time()))
            self.target(*self.args)




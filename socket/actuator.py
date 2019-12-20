from configuration import configValue
from scheduler import agentScheduler
from threading import Thread
from queue import Queue
import apiAgent
import fileAgent


if __name__ == '__main__':
    q = Queue()
    number = configValue(config = 'config.in',sections='Scheduler')
    aa = number.getValue()['time']
    diaodu = agentScheduler(schedulingCycle = int(aa),queue=q,target=apiAgent.api,args=('fff',))
    diaodu2 = agentScheduler(schedulingCycle = int(aa),queue=q,target=fileAgent.file,args=('fff',))
    tt = Thread(target=diaodu.scheduling)
    tt.start()
    while True:
        print(q.get(1))



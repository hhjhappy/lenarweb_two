import configparser
import threading
from queue import Queue
import time

def get_html(queue,a):
    while True:
        queue.put(a)
        print('get detail html started')
        time.sleep(3)
        print('get detail html end')

def get_url(queue):
    while True:
        print('get detail url started')
        print(queue.get(1))
        time.sleep(1)
        print('get detail url end')
    
if __name__ == '__main__':
    url_queue = Queue(maxsize=1000)
    thread2 = threading.Thread(target=get_url,args=(url_queue,))
    thread2.start()
    for i in range(2):
        thread1 = threading.Thread(target=get_html,args=(url_queue,'fff'))
        thread1.start()

    start_time = time.time()


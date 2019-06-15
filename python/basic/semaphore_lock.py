import gevent
from requests import get
from gevent.monkey import patch_all; patch_all()

from gevent.lock import Semaphore

sem = Semaphore()

def f1():
    sem.acquire()
    print("Thread 1 start")
    gevent.sleep(0.1)
    print("Thread 1 end")
    sem.release()

def f2():
    with sem:
        print("Thread 2")
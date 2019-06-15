import gevent
from semaphore_lock import f1, f2

gevent.joinall([
    gevent.spawn(f1),
    gevent.spawn(f1)
])
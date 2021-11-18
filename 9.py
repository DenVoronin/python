import time
from threading import Thread

def test (i):
    print("Thread %i wakeup\n" % i)
    for y in range(10):
        print("Thread %i:"% i + str(y))
    
    time.sleep(1)
    print("thread %i sleep\n" % i)

for i in range(2):
    th = Thread(target=test, args=(i, ))
    th.start()

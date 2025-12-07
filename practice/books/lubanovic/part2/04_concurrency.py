import multiprocessing as mp
import random
from datetime import datetime as dt
import time


# 15.1
def show_random():
    time.sleep(random.random())
    print(dt.now().time().strftime('%H:%M:%S'))


if __name__ == '__main__':
    procs = []
    for i in range(3):
        proc = mp.Process(target=show_random)
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

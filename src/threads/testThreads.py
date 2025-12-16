import random
import threading
import time

from typing import List



def myFunc(thread_number:int, delay:float):    
    time.sleep(delay)
    return print('My func by thread N° \'{}\''.format(thread_number))


def main():
    allThreads: List[threading.Thread] = []    
    for i in range(10):
        delay:float = random.random()
        newThread   = threading.Thread(target=myFunc, args=(i,delay))
        allThreads.append(newThread)        
    
    for i in range(10):
        allThreads[i].start()
        
    for i in range(10):
        allThreads[i].join()


if __name__ == '__main__':
    main()
    
    
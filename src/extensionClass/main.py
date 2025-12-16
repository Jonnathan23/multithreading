import time
from random import randint

from ExtensionThread import MyThreadClass



start_time = time.time()

# Thread Creation
thread1 = MyThreadClass("Experiment_1", randint(1,10))
thread2 = MyThreadClass("Exp_2", randint(1,10))
thread3 = MyThreadClass("Exper_3", randint(1,10))
thread4 = MyThreadClass("ment_4", randint(1,10))
thread5 = MyThreadClass("Experi_5", randint(1,10))
thread6 = MyThreadClass("Expt_6", randint(1,10))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()

print('End')

print(f'Tiempo de ejecución: {time.time() - start_time:.6f} segundos')
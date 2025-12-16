import threading
import numpy as np
import time
from typing import List
import math 


class Parallel: 
    def __init__(self, dimension: int, num_threads: int = 1) -> None:
        self.dimension   : int = dimension
        self.num_threads : int = num_threads
        
        self.matA: np.ndarray = np.random.randint(0, 10, (self.dimension, self.dimension))
        self.matB: np.ndarray = np.random.randint(0, 10, (self.dimension, self.dimension))
        self.matC: np.ndarray = np.zeros((self.dimension, self.dimension))
        self.finalTime: float = 0.0

        # Para que el sleep no haga que el test dure 20000 segundos, reducimos la dimensión 
        # para esta visualización.
        if self.dimension > 100:
             print("ADVERTENCIA: La dimensión es grande. Reduzca la dimensión o quite el time.sleep(2).")

        print(f"Matrices de {dimension}x{dimension}. Usando {self.num_threads} hilos.")

    def sumMatrices(self) -> None:
        
        allThreads: List[threading.Thread] = []
        startTime: float = time.time()
        
        rows_per_thread: int = math.ceil(self.dimension / self.num_threads)
        
        for t_id in range(self.num_threads):
            start_row: int = t_id * rows_per_thread
            
            if start_row >= self.dimension:
                break
            
            end_row: int = min((t_id + 1) * rows_per_thread, self.dimension)
            
            # Crear el hilo
            newThread: threading.Thread = threading.Thread(
                target=self.sumRows, 
                args=(start_row, end_row)
            )
            
            allThreads.append(newThread)
            newThread.start()
            
        # 2. FASE DE ESPERA/JOIN
        for thread in allThreads:
            thread.join()
            
        self.finalTime = self.showTime(startTime)

    def sumRows(self, start_row: int, end_row: int) -> None: 
        """
        Método corregido para usar las convenciones modernas de threading.
        """
        
        # 1. Corregido: currentThread() -> current_thread()
        # 2. Corregido: .getName() -> .name
        thread_name = threading.current_thread().name # Obtener el nombre del hilo de forma moderna
        
        # 1. Logging de inicio
        print(f"{thread_name} --> starting (Rows: {start_row}-{end_row})")
        
        # 2. Dormir el hilo por 2 segundos (Simular carga pesada)
        time.sleep(2) 
        
        # 3. La operación principal: Suma de matrices
        for i in range(start_row, end_row):
            for j in range(self.dimension):
                self.matC[i][j] = self.matA[i][j] + self.matB[i][j]
                
        # 4. Logging de finalización
        print(f"{thread_name} --> exiting")
        
            
    def showTime(self, startTime: float) -> float: 
        endTime: float = time.time()
        finalTime: float = endTime - startTime 
        return finalTime
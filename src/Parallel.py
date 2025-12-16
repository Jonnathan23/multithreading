import threading
import numpy as np
import time
# Importamos List y math (asumo que math ya estaba importado, si no, es necesario)
from typing import List, Optional
import math 


class Parallel: 
    def __init__(self, dimension: int, num_threads: int = 1) -> None:
        self.dimension   : int = dimension
        self.num_threads : int = num_threads
        
        self.matA: np.ndarray = np.random.randint(0, 10, (self.dimension, self.dimension))
        self.matB: np.ndarray = np.random.randint(0, 10, (self.dimension, self.dimension))
        self.matC: np.ndarray = np.zeros((self.dimension, self.dimension))
        self.finalTime: float = 0.0

        print(f"Matrices de {dimension}x{dimension}. Usando {self.num_threads} hilos.")

    def sumMatrices(self) -> None:
        
        allThreads: List[threading.Thread] = []
        startTime: float = time.time()
        
        rows_per_thread: int = math.ceil(self.dimension / self.num_threads)
        
        for t_id in range(self.num_threads):
            start_row: int = t_id * rows_per_thread
            if start_row >= self.dimension:
                break
            
            # Calcular la fila de fin (limitada por la dimensión total)
            end_row: int = min((t_id + 1) * rows_per_thread, self.dimension)
            
            newThread: threading.Thread = threading.Thread(
                target=self.sumRows, 
                args=(start_row, end_row)
            )
            
            allThreads.append(newThread)
            newThread.start()
            
        # 2. FASE DE ESPERA/JOIN
        for thread in allThreads:
            thread.join()
            
        # Almacenar el tiempo final
        self.finalTime = self.showTime(startTime)

    def sumRows(self, start_row: int, end_row: int) -> None:         
        for i in range(start_row, end_row):
            for j in range(self.dimension):
                self.matC[i][j] = self.matA[i][j] + self.matB[i][j]
                
    
    def showTime(self, startTime: float) -> float:    
        endTime: float = time.time()
        finalTime: float = endTime - startTime      
        return finalTime
    
    
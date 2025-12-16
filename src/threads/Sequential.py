import numpy as np
import time


class Sequential:
    def __init__(self, dimention:int):
        self.dimention = dimention
        self.matA = np.random.randint(0,10,(self.dimention,self.dimention))
        self.matB = np.random.randint(0,10,(self.dimention,self.dimention))
        self.matC = np.zeros((self.dimention,self.dimention))
        self.finalTime:float = 0
        
    
    def sumMatrices(self):
        print(f"Matrices de {self.dimention}x{self.dimention}")
        start_time = time.time()
        for i in range(self.dimention):
            for j in range(self.dimention):
                self.matC[i][j] = self.matA[i][j] + self.matB[i][j]
        self.finalTime = self.showTime(start_time)
        #self.showMatrices()    

    def showMatrices(self) -> None:
        print("Matriz A: \n", self.matA)
        print("Matriz B: \n", self.matB)
        print("Matriz C: \n", self.matC)
    
    def showTime(self, startTime:float) -> float:
        endTime = time.time()
        finalTime = endTime - startTime      
        print(f'Tiempo de ejecución: {finalTime:.6f} segundos')  
        return finalTime
        
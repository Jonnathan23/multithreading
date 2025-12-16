import os
from typing import List, Tuple

from Parallel import Parallel
from Sequential import Sequential
from utils.utils import showTableTimeComparative




DIMENSION = 100

# 1. Crear y ejecutar todas las instancias
secuencial = Sequential(DIMENSION)
secuencial.sumMatrices()

NUM_CORES: int = os.cpu_count() or 4 # Obtener el número máximo de núcleos

print(f"\n--- INICIANDO EXPERIMENTO ---")
print(f"Sistema con {NUM_CORES} núcleos lógicos.")

# Lista para almacenar todos los resultados (Nombre, Tiempo, Procesos)
results: List[Tuple[str, float, int]] = []


# 1. EJECUCIÓN SECUENCIAL (Línea Base)
print("\n[1/5] Ejecutando Secuencial...")
secuencial = Sequential(DIMENSION)
secuencial.sumMatrices()
results.append(("Secuencial (Base)", secuencial.finalTime, 1))


# 2. EJECUCIÓN PARALELA con 2 Procesos
print("\n[2/5] Ejecutando Paralelo con 2 procesos...")
paralelo2 = Parallel(DIMENSION, 2)
paralelo2.sumMatrices()
results.append(("Paralelo (2 Proc)", paralelo2.finalTime, 2))


# 3. EJECUCIÓN PARALELA con 4 Procesos
print("\n[3/5] Ejecutando Paralelo con 4 procesos...")
paralelo4 = Parallel(DIMENSION, 4)
paralelo4.sumMatrices()
results.append(("Paralelo (4 Proc)", paralelo4.finalTime, 4))


# 4. EJECUCIÓN PARALELA con 8 Procesos
print("\n[4/5] Ejecutando Paralelo con 8 procesos...")
paralelo8 = Parallel(DIMENSION, 8)
paralelo8.sumMatrices()
results.append(("Paralelo (8 Proc)", paralelo8.finalTime, 8))


# 6. MOSTRAR LA TABLA COMPARATIVA
print("\n--- FINALIZANDO EXPERIMENTO ---")
showTableTimeComparative(results, DIMENSION)
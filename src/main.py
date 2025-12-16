#from typing import List
#from tabulate import tabulate

#import Parallel
from Sequential import Sequential



'''

def showTableTimeComparative(data: List[Tuple[str, float, int]]) -> None:
    """
    Genera y muestra una tabla comparativa de tiempos de ejecución.

    Args:
        data: Una lista de tuplas con (Nombre del Test, Tiempo, Número de Hilos).
    """
    
    # 1. Definir los encabezados de la tabla
    headers = ["Test", "Hilos", "Tiempo (segundos)"]
    
    # 2. Convertir la lista de tuplas a formato de tabla (Lista de listas)
    table_data = []
    for name, time_val, threads in data:
        # Añadimos los datos, formateando el tiempo a 6 decimales para precisión
        table_data.append([name, threads, f"{time_val:.6f}"])
    
    # 3. Imprimir la tabla usando la librería 'tabulate' (si está instalada)
    try:
        print("\n" + "="*50)
        print("         📊 COMPARATIVA DE TIEMPOS DE EJECUCIÓN 📊")
        print("="*50)
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", numalign="center", stralign="left"))
        print(f"\nNota: Todos los tests se ejecutaron con una dimensión de matriz de {DIMENSION}x{DIMENSION}.")
        
    # Si 'tabulate' no está instalada, imprime una tabla simple
    except ImportError:
        print("\n--- COMPARATIVA DE TIEMPOS DE EJECUCIÓN ---")
        print(f"{'Test':<20} | {'Hilos':<5} | {'Tiempo (segundos)':<18}")
        print("-" * 47)
        for name, time_val, threads in data:
            print(f"{name:<20} | {threads:<5} | {time_val:<.6f}")
        print("-" * 47)
    
'''

DIMENSION = 10000

# 1. Crear y ejecutar todas las instancias
secuencial = Sequential(DIMENSION)
secuencial.sumMatrices()

#paralelo1 = Parallel(DIMENSION, 1) # Paralelo con 1 hilo
#paralelo1.sumMatrices()
#
#paralelo4 = Parallel(DIMENSION, 4)
#paralelo4.sumMatrices()
#
#paralelo8 = Parallel(DIMENSION, 8)
#paralelo8.sumMatrices()

# Aquí puedes añadir más pruebas, como el número de núcleos de tu CPU
# paralelo_max = Parallel(DIMENSION, os.cpu_count() or 8)
# paralelo_max.sumMatrices()


# 2. Recolectar los resultados en el formato: (Nombre, Tiempo, Hilos)
#results = [
#    ("Secuencial (Base)", secuencial.finalTime, 1),
#    ("Paralelo (1 Hilo)", paralelo1.finalTime, 1), # Usar 'paralelo1' en lugar de 'paralelo'
#    ("Paralelo (4 Hilos)", paralelo4.finalTime, 4),
#    ("Paralelo (8 Hilos)", paralelo8.finalTime, 8),
#    # ("Paralelo (Máx Hilos)", paralelo_max.finalTime, paralelo_max.num_threads),
#]

# 3. Mostrar la tabla comparativa
#showTableTimeComparative(results)
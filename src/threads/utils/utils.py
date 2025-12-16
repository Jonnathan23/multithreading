from typing import List, Tuple


def showTableTimeComparative(data: List[Tuple[str, float, int]], DIMENSION: int) -> None:
    print("\n--- COMPARATIVA DE TIEMPOS DE EJECUCIÓN ---")
    print(f"{'Test':<20} | {'Procesos':<8} | {'Tiempo (segundos)':<18}")
    print("-" * 50)
    for name, time_val, processes in data:
        # Usamos 'processes' en lugar de 'hilos'
        print(f"{name:<20} | {processes:<8} | {time_val:.6f}")
    print("-" * 50)
    print(f"Dimensión: {DIMENSION}x{DIMENSION}")
    print("El rendimiento de la versión Paralela refleja el uso de multiprocessing (paralelismo real).")


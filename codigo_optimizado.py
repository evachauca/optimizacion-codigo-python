import time
import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

inicio = time.time()

primos = [num for num in range(1, 100000) if es_primo(num)]

fin = time.time()

print("Cantidad de primos:", len(primos))
print("Tiempo de ejecución:", fin - inicio)

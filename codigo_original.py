import time

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

inicio = time.time()

primos = []
for num in range(1, 100000):
    if es_primo(num):
        primos.append(num)

fin = time.time()

print("Cantidad de primos:", len(primos))
print("Tiempo de ejecución:", fin - inicio)

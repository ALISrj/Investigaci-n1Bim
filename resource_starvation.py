# import threading
# import time

# # Recurso compartido (semáforo)
# semaforo = threading.Semaphore(0)

# def filosofo(nombre, tenedor):
#     semaforo.acquire()  # Esperando por un tenedor
#     print(f"{nombre} tomó el tenedor {tenedor}")
#     time.sleep(1)  # Comiendo
#     print(f"{nombre} dejó el tenedor {tenedor}")
#     semaforo.release()  # Liberando el tenedor

# filosofos = ['Aristóteles', 'Platón', 'Sócrates']
# tenedores = [1, 5, 9]

# hilos = []
# for i in range(3):
#     t = threading.Thread(target=filosofo, args=(filosofos[i], tenedores[i]))
#     hilos.append(t)
#     t.start()

# for t in hilos:
#     t.join()

# print("Todos los filósofos han comido.")

import threading
import time
import random

# Número de tenedores (recursos)
N = 3  # Número de tenedores

# Recurso compartido (tenedores)
tenedores = [threading.Semaphore(1) for _ in range(N)]

def filosofo(nombre):
    while True:
        # Tomar un tenedor aleatorio
        tenedor = random.randint(0, N - 1)
        if tenedores[tenedor].acquire(blocking=False):
            print(f"{nombre} tomó el tenedor {tenedor}")
            time.sleep(1)  # Comiendo
            print(f"{nombre} dejó el tenedor {tenedor}")
            tenedores[tenedor].release()
            break  # Comer una vez y terminar
        else:
            time.sleep(0.1)  # Esperar un poco antes de intentar nuevamente

filosofos = ['Filósofo 1', 'Filósofo 2', 'Filósofo 3', 'Filósofo 4', 'Filósofo 5']

hilos = []
for nombre in filosofos:
    t = threading.Thread(target=filosofo, args=(nombre,))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

print("Todos los filósofos han comido.")
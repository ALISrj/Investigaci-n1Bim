import threading
import time

# Variable compartida
contador = 0

# Bloqueo para proteger el acceso al contador
lock = threading.Lock()

def incrementar_contador():
    global contador
    time.sleep(1)

    #with lock:
    local_counter = contador
    local_counter += 1

    contador = local_counter
    print(f"Contador incrementado: {contador}")



# Crear y iniciar varios subprocesos
runs = []
for _ in range(10):
    run = threading.Thread(target=incrementar_contador)
    runs.append(run)
    run.start()

# Esperar a que todos los subprocesos finalicen
for run in runs:
    run.join()

print(f"Valor final del contador: {contador}")

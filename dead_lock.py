import threading
import time

# Crear dos bloqueos
lock1 = threading.Lock()
lock2 = threading.Lock()

def worker1():
    # Adquirir los bloqueos en el orden predefinido
    lock1.acquire()
    print("Worker 1 adquirió el bloqueo 1")
    
    time.sleep(1)  # Simular algún trabajo
    
    lock2.acquire()
    print("Worker 1 adquirió el bloqueo 2")
    
    # Liberar los bloqueos en orden inverso
    lock2.release()
    lock1.release()

def worker2():
    # Adquirir los bloqueos en el mismo orden predefinido
    lock1.acquire()
    print("Worker 2 adquirió el bloqueo 1")
    
    time.sleep(1)  # Simular algún trabajo
    
    lock2.acquire()
    print("Worker 2 adquirió el bloqueo 2")
    
    # Liberar los bloqueos en orden inverso
    lock2.release()
    lock1.release()

# Crear y iniciar los subprocesos
worker1 = threading.Thread(target=worker1)
worker2 = threading.Thread(target=worker2)

worker1.start()
worker2.start()

# Esperar a que los subprocesos finalicen
worker1.join()
worker2.join()

print("Fin del programa")
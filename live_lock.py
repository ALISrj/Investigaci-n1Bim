def problem():    
    import threading
    import time

    # Crear dos bloqueos
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def worker1():
        while True:
            # Intentar adquirir el primer bloqueo
            lock1.acquire()
            print("Worker 1 adquirió el bloqueo 1")
            
            # Esperar un poco para simular algún trabajo
            time.sleep(1)
            
            # Intentar adquirir el segundo bloqueo
            print("Worker 1 intentando adquirir el bloqueo 2")
            if lock2.acquire(timeout=1):  # Esperar como máximo 1 segundo
                print("Worker 1 adquirió el bloqueo 2")
                
                # Liberar los bloqueos
                lock2.release()
                lock1.release()
            else:
                print("Worker 1 no pudo adquirir el bloqueo 2, intentando de nuevo")
                lock1.release()

    def worker2():
        while True:
            # Intentar adquirir el segundo bloqueo
            lock2.acquire()
            print("Worker 2 adquirió el bloqueo 2")
            
            # Esperar un poco para simular algún trabajo
            time.sleep(1)
            
            # Intentar adquirir el primer bloqueo
            print("Worker 2 intentando adquirir el bloqueo 1")
            if lock1.acquire(timeout=1):  # Esperar como máximo 1 segundo
                print("Worker 2 adquirió el bloqueo 1")
                
                # Liberar los bloqueos
                lock1.release()
                lock2.release()
            else:
                print("Worker 2 no pudo adquirir el bloqueo 1, intentando de nuevo")
                lock2.release()

    # Crear y iniciar los subprocesos
    worker1 = threading.Thread(target=worker1)
    worker2 = threading.Thread(target=worker2)

    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()

def solution():
    import threading
    import time

    # Crear tres bloqueos
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock_arbiter = threading.Lock()  # Bloqueo árbitro

    def worker1():
        while True:
            # Adquirir el bloqueo árbitro
            with lock_arbiter:
                # Intentar adquirir los bloqueos principales en un orden definido
                lock1.acquire()
                print("Worker 1 adquirió el bloqueo 1")
                time.sleep(1)  # Simular algún trabajo
                
                lock2.acquire()
                print("Worker 1 adquirió el bloqueo 2")
                
                # Liberar los bloqueos principales en orden inverso
                lock2.release()
                lock1.release()

    def worker2():
        while True:
            # Adquirir el bloqueo árbitro
            with lock_arbiter:
                # Intentar adquirir los bloqueos principales en el mismo orden definido
                lock1.acquire()
                print("Worker 2 adquirió el bloqueo 1")
                time.sleep(1)  # Simular algún trabajo
                
                lock2.acquire()
                print("Worker 2 adquirió el bloqueo 2")
                
                # Liberar los bloqueos principales en orden inverso
                lock2.release()
                lock1.release()

    # Crear y iniciar los subprocesos
    worker1 = threading.Thread(target=worker1)
    worker2 = threading.Thread(target=worker2)

    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()


problem()
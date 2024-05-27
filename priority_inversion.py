def problem():
    import threading
    import time

    # Recurso compartido
    recurso = threading.Lock()

    # Hilo de alta prioridad
    class HiloAltaPrioridad(threading.Thread):
        def run(self):
            print("Hilo de alta prioridad esperando el recurso...")
            recurso.acquire()
            print("Hilo de alta prioridad adquirió el recurso.")
            time.sleep(5)  # Simula un trabajo de larga duración
            recurso.release()
            print("Hilo de alta prioridad finalizó.")

    # Hilo de baja prioridad
    class HiloBajaPrioridad(threading.Thread):
        def run(self):
            print("Hilo de baja prioridad esperando el recurso...")
            recurso.acquire()
            print("Hilo de baja prioridad adquirió el recurso.")
            time.sleep(1)  # Simula un trabajo corto
            recurso.release()
            print("Hilo de baja prioridad finalizó.")

    # Hilo de prioridad media
    class HiloMediaPrioridad(threading.Thread):
        def run(self):
            print("Hilo de prioridad media esperando el recurso...")
            recurso.acquire()
            print("Hilo de prioridad media adquirió el recurso.")
            time.sleep(3)  # Simula un trabajo de duración media
            recurso.release()
            print("Hilo de prioridad media finalizó.")

    # Creación de hilos
    hilo_alta_prioridad = HiloAltaPrioridad()
    hilo_baja_prioridad = HiloBajaPrioridad()
    hilo_media_prioridad = HiloMediaPrioridad()

    # Configuración de prioridades
    hilo_alta_prioridad.priority = 10  # Alta prioridad
    hilo_baja_prioridad.priority = 1   # Baja prioridad
    hilo_media_prioridad.priority = 5  # Prioridad media

    # Inicio de hilos
    hilo_baja_prioridad.start()
    hilo_media_prioridad.start()
    hilo_alta_prioridad.start()

    # Espera a que finalicen los hilos
    hilo_alta_prioridad.join()
    hilo_baja_prioridad.join()
    hilo_media_prioridad.join()

    print("Programa finalizado.")

def solution():
    import threading
    import time

    # Recurso compartido
    recurso = threading.Lock()

    # Evento para controlar la ejecución del hilo de alta prioridad
    evento_alta_prioridad = threading.Event()

    # Hilo de alta prioridad
    class HiloAltaPrioridad(threading.Thread):
        def run(self):
            print("Hilo de alta prioridad esperando el recurso...")
            with recurso:
                print("Hilo de alta prioridad adquirió el recurso.")
                time.sleep(5)  # Simula un trabajo de larga duración
            print("Hilo de alta prioridad finalizó.")
            evento_alta_prioridad.set()  # Permite la ejecución de los demás hilos

    # Hilo de baja prioridad
    class HiloBajaPrioridad(threading.Thread):
        def run(self):
            print("Hilo de baja prioridad esperando el recurso...")
            evento_alta_prioridad.wait()  # Espera hasta que se complete el hilo de alta prioridad
            with recurso:
                print("Hilo de baja prioridad adquirió el recurso.")
                time.sleep(1)  # Simula un trabajo corto
            print("Hilo de baja prioridad finalizó.")

    # Hilo de prioridad media
    class HiloMediaPrioridad(threading.Thread):
        def run(self):
            print("Hilo de prioridad media esperando el recurso...")
            evento_alta_prioridad.wait()  # Espera hasta que se complete el hilo de alta prioridad
            with recurso:
                print("Hilo de prioridad media adquirió el recurso.")
                time.sleep(3)  # Simula un trabajo de duración media
            print("Hilo de prioridad media finalizó.")

    # Creación de hilos
    hilo_alta_prioridad = HiloAltaPrioridad()
    hilo_baja_prioridad = HiloBajaPrioridad()
    hilo_media_prioridad = HiloMediaPrioridad()

    # Inicio de hilos
    hilo_baja_prioridad.start()
    hilo_media_prioridad.start()
    hilo_alta_prioridad.start()

    # Espera a que finalicen los hilos
    hilo_alta_prioridad.join()
    hilo_baja_prioridad.join()
    hilo_media_prioridad.join()

    print("Programa finalizado.")

solution()
# import threading
# import time

# # Recurso compartido
# recurso = threading.Lock()

# # Hilo de alta prioridad
# class HiloAltaPrioridad(threading.Thread):
#     def run(self):
#         print("Hilo de alta prioridad adquiriendo el recurso...")
#         recurso.acquire()
#         print("Hilo de alta prioridad en ejecución...")
#         time.sleep(5)  # Simula un trabajo de larga duración
#         recurso.release()
#         print("Hilo de alta prioridad finalizó.")

# # Hilo de baja prioridad
# class HiloBajaPrioridad(threading.Thread):
#     def run(self):
#         print("Hilo de baja prioridad adquiriendo el recurso...")
#         recurso.acquire()
#         print("Hilo de baja prioridad en ejecución...")
#         recurso.release()
#         print("Hilo de baja prioridad finalizó.")

# # Hilo de prioridad media
# class HiloMediaPrioridad(threading.Thread):
#     def run(self):
#         print("Hilo de prioridad media adquiriendo el recurso...")
#         recurso.acquire()
#         print("Hilo de prioridad media en ejecución...")
#         recurso.release()
#         print("Hilo de prioridad media finalizó.")

# # Creación de hilos
# hilo_alta_prioridad = HiloAltaPrioridad()
# hilo_baja_prioridad = HiloBajaPrioridad()
# hilo_media_prioridad = HiloMediaPrioridad()

# # Configuración de prioridades
# hilo_alta_prioridad.priority = 10  # Alta prioridad
# hilo_baja_prioridad.priority = 1   # Baja prioridad
# hilo_media_prioridad.priority = 5  # Prioridad media

# # Inicio de hilos
# hilo_baja_prioridad.start()
# hilo_media_prioridad.start()
# hilo_alta_prioridad.start()

# # Espera a que finalicen los hilos
# hilo_alta_prioridad.join()
# hilo_baja_prioridad.join()
# hilo_media_prioridad.join()

# print("Programa finalizado.")


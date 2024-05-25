import multiprocessing

def tarea() :
    resultado = 0
    for _ in range(10):
        resultado += 1
        print(resultado, flush=True)
    return resultado

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=tarea)
    p2 = multiprocessing.Process(target=tarea)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("tarea terminada")

import time
import ray

def fibonacci_local(tam):
    fibonacci = []
    for i in range(0, tam):
        if i < 2:
            fibonacci.append(i)
            continue
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return tam

@ray.remote
def fibonacci_distribuido(tam):
    fibonacci = []
    for i in range(0, tam):
        if i < 2:
            fibonacci.append(i)
            continue
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return tam
    
def correr_local(tam):
    tiempo_inicial = time.time()
    resultado = [fibonacci_local(tam) for _ in range(3)]
    duracion = time.time() - tiempo_inicial
    print("Tamanio de secuencia: {}, Tiempo de ejecucion local: {}".format(tam, duracion))

def correr_remoto(tam):
    ray.init()
    tiempo_inicial = time.time()
    resultado = ray.get([fibonacci_local(tam) for _ in range(3)])
    duracion = time.time() - tiempo_inicial
    print("Tamanio de secuencia: {}, Tiempo de ejecucion local: {}".format(tam, duracion))

correr_local(80000)
correr_remoto(80000)
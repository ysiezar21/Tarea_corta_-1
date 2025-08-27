import random
import time         # Para medir el tiempo
import tracemalloc  # Para medir memoria

"""
Nombre: generar_matriz
Entrada: Número entero (num)
Salida: Una matriz de tamaño num x num con números enteros aleatorios entre 0 y 1000
Descripción: 
    Genera una matriz cuadrada con valores enteros aleatorios.
"""
def generar_matriz(num):
    return [[random.randint(0, 1000) for i in range(num)] for j in range(num)]

"""
Nombre: medidor_rendimiento
Entrada: 
    - matriz : matriz nxn con números enteros
    - metodo (str): tipo de algoritmo de ordenamiento ("quicksort" o "mergesort")
Salida: 
    - matriz ordenada
    - tiempo de ejecución 
    - memoria utilizada en MB
Descripción: 
    Ejecuta el algoritmo de ordenamiento seleccionado sobre la matriz, 
    midiendo el tiempo de ejecución y la memoria consumida.
"""
def medidor_rendimiento(matriz, metodo):
    if metodo != "quicksort" and metodo != "mergesort":
        return "ERROR: Metodo de ordenamiento seleccionado incorrecto, por favor escribir solo quicksort o mergesort"
    
    tracemalloc.start() # Aqui se mide la memoria
    inicio = time.time() # Iniciar medición de tiempo

    resultado = ordenar_Matriz(matriz, metodo);
    
    fin = time.time() # Fin de medición de tiempo
    memoria = tracemalloc.get_traced_memory()[1] / (1024*1024) # Memoria en MB
    tracemalloc.stop()
    tiempo = fin - inicio
    return resultado, tiempo, memoria

"""
Nombre: quicksort_lista
Entrada: lista desordenada 
Salida: lista ordenada  
Descripción: 
    Ordena una lista utilizando el algoritmo quicksort de manera recursiva.
"""
def quicksort_lista(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[-1] # Acá se elige el último elemento como pivote
    menores = [x for x in lista[:-1] if x <= pivote]
    mayores = [x for x in lista[:-1] if x > pivote]
    return quicksort_lista(menores) + [pivote] + quicksort_lista(mayores)

"""
Nombre: quicksort
Entrada: matriz nxn 
Salida: matriz con cada fila ordenada 
Descripción: 
    Aplica quicksort a cada fila de la matriz de forma independiente.
"""
def quicksort(matriz):
    return [quicksort_lista(fila) for fila in matriz]

"""
Nombre: mergesort_lista
Entrada: lista desordenada (list[int])
Salida: lista ordenada (list[int])
Descripción: 
    Ordena una lista utilizando el algoritmo mergesort de manera recursiva.
"""
def mergesort_lista(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort_lista(lista[:medio])
    derecha = mergesort_lista(lista[medio:])
    return merge(izquierda, derecha)

"""
Nombre: merge
Entrada: 
    - izquierda (list[int])
    - derecha (list[int])
Salida: lista ordenada (list[int])
Descripción: 
    Mezcla dos listas previamente ordenadas en una sola lista ordenada.
"""
def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

"""
Nombre: mergesort
Entrada: matriz nxn (list[list[int]])
Salida: matriz con cada fila ordenada (list[list[int]])
Descripción: 
    Aplica mergesort a cada fila de la matriz de forma independiente.
"""
def mergesort(matriz):
    return [mergesort_lista(fila) for fila in matriz]

"""
Nombre: ordenar_Matriz
Entrada: 
    - matriz (list[list[int]])
    - metodo (str): "quicksort" o "mergesort"
Salida: matriz ordenada (list[list[int]])
Descripción: 
    Aplica el método de ordenamiento seleccionado sobre la matriz.
"""
def ordenar_Matriz(matriz, metodo):
    resultado = [] #Acá va a estar la matriz ya ordenada

    if metodo == 'quicksort':           # Comparaciones para identificar el metodo de ordenamiento
        resultado = quicksort(matriz)
    elif metodo == 'mergesort':
        resultado = mergesort(matriz)
    else :
        print("ERROR: Metodo/Algoritmo de ordenamiento seleccionado es incorrecto") # print en caso de error

    return resultado


# =========================
# Pruebas para diferentes tamaños
# =========================
n = 1000
print(f"\n===== Tamaño: {n}x{n} =====")
matriz = generar_matriz(n)

# QuickSort
matriz_final, tiempo_qs, memoria_qs = medidor_rendimiento(matriz, 'quicksort')
print("QuickSort -> Tiempo: ", tiempo_qs, " Memoria: ", memoria_qs, " MB")

#Mergesort
matriz_final, tiempo_qs, memoria_qs = medidor_rendimiento(matriz, 'mergesort')
print("MergeSort -> Tiempo: ", tiempo_qs, " Memoria: ", memoria_qs, " MB")

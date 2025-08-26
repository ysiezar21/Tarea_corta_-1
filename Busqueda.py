
import random
import time
import tracemalloc

# Entradas: Una matriz de nxn elementos y un elemento x a encontrar
# Salidas: 'Encontrado' si encuentra el numero a buscar, 'No encontrado' si no encuentra el numero
# Restricciones: La matriz debe ser cuadrada y debe tener solo numeros enteros, el numero x debe ser entero

def busqueda_hash(matriz, x):
    tabla = {}                                       # 1
    largo = len(matriz)                              # 1
    
    for i in range(largo):                           # n
        for j in range(largo):                       # n
            valor = matriz[i][j]                     # 1
            tabla[valor] = (i, j)                    # 1
    
    if x in tabla:                                   # 1
        return "Encontrado"                          # 1
    else:                                            # 1
        return "No encontrado"                       # 1
    

# Entradas: Una matriz de nxn elementos y un elemento x a encontrar
# Salidas: 'Encontrado' si encuentra el numero a buscar, 'No encontrado' si no encuentra el numero
# Restricciones: La matriz debe ser cuadrada y debe tener solo numeros enteros, el numero x debe ser entero

def busqueda_lineal(m,x):
    for i in m:
        for j in i:
            if j == x:
                return "Encontrado"
    return "No encontrado"

# Entradas: Un valor n que indica la cantidad de filas y columnas de la matriz
# Salidas: Una matriz de nxn elementos los cuales son numeros enteros entre 0 y 99
# Restricciones: El valor n debe ser un numero entero mayor o igual a 1

def generar_matriz(n):
    if n >= 1:
        matriz = [] 
        
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(random.randint(0, 99))
            matriz.append(fila)
        return matriz
    else:
        print("El tamaño de la matriz debe ser de 1x1 o mayor")


# Pruebas:
nxn = 10
x = 39
matriz = generar_matriz(nxn)
print("Tamaño de matriz:", nxn, "x", nxn)
print("Numero buscado: ", x)
print("")

print("Busqueda Hash:")
inicio = time.time()
tracemalloc.start()

print(busqueda_hash(matriz,x))

fin = time.time()
memoria_actual, memoria_max = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Tiempo de ejecución:", fin - inicio, "segundos")
print("Memoria usada:", memoria_max / 1024, "KB")


print("")
print("Busqueda lineal:")
inicio2 = time.time()
tracemalloc.start()

print(busqueda_lineal(matriz,x))

fin2 = time.time()
memoria_actual2, memoria_max2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Tiempo de ejecución:", fin2 - inicio2, "segundos")
print("Memoria usada:", memoria_max2 / 1024, "KB")

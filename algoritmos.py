import math
from collections import deque



def distancia_euclidiana(x_1, y_1, x_2, y_2):
    #Calcula la distancia euclidiana
    res = int(math.sqrt( ( pow((x_2 - x_1), 2) ) + ( pow((y_2 - y_1), 2) ) ) )
	#Devuelve el resultado de la fórmula 
    return res

	#También se le conoce a la fórmula como:
	#distancia entre dos puntos

def busqueda_profundidad(grafo, origen):

    visitados = []
    stack = deque()
    recorrido = []

    visitados.append(origen)
    stack.append(origen)

    while stack:
        vertice = stack.pop()
        recorrido.append(vertice)

        adyacentes = grafo[vertice]
        #Revisar vertices adyacentes
        for adyacente  in adyacentes:
            #Validar que no este visitado
            ady = adyacente[0]
            if ady not in visitados:
                visitados.append(ady)
                stack.append(ady)

    return recorrido        


def busqueda_amplitud(grafo, origen):

    visitados = []
    queue = deque()
    recorrido = []

    visitados.append(origen)
    queue.append(origen)

    while queue:
        vertice = queue.pop()
        recorrido.append(vertice)
        #obtener la lista de adyacente del vertice actual
        adyacentes = grafo[vertice]

        #Revisar los vertices adyacentes
        for adyacente  in adyacentes:
            #obtener solo el vertice, no el peso: adyacente[0]
            ady = adyacente[0]
            #Validar que no este visitado
            if ady not in visitados:
                visitados.append(ady)
                queue.appendleft(ady)

    return recorrido     
from particula import Particula
from algoritmos import busqueda_profundidad, busqueda_amplitud
from pprint import pprint, pformat
import json

class Administradora:
    def __init__(self):
        self.__particulas = []
        self.__grafo = dict()

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
        self.agregar_grafo(particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
        self.agregar_grafo(particula)
        
    def agregar_grafo(self, particula:Particula):
        origen = (particula.origen_x, particula.origen_y)
        destino = (particula.destino_x, particula.destino_y)

        arista_o_d = (destino, particula.distancia)
        arista_d_o = (origen, particula.distancia)

        if origen in self.__grafo:
            self.__grafo[origen].append(arista_o_d)
        else:
            self.__grafo[origen] = [arista_o_d]

        if destino in self.__grafo:
            self.__grafo[destino].append(arista_d_o)
        else:
            self.__grafo[destino] = [arista_d_o]

    def mostrar(self):
        #for particula in self.__particulas:
        #    print(particula)

        string = pformat(self.__grafo, width=60, indent=1)
        return string
        
    def __str__(self):
        #join recibe n cantidad de elementos para meter a ese string
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def guardar(self,ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista,archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                #self.__grafo = json.load(archivo)
                #Los dos asteriscos los convierte los datos json a parametros
                self.__particulas = [Particula(**particula) for particula in lista]

                self.__grafo.clear()

                for particula in self.__particulas:
                    self.agregar_grafo(particula)


            return 1
        except:
            return 0
    
    def __len__(self):
        return len(self.__particulas)
    
    #Crear un iterador
    def __iter__(self):
        #retorna el contador
        self.cont = 0
        return self

    def __next__(self):
        #siguiente elemento
        if self.cont < len(self.__particulas):
            #se guarda el elemento en la posicion que indique el contador
            particula = self.__particulas[self.cont]
            #antes de retornar se incrementa el contador
            self.cont += 1
            return particula
        else:
            #deja de continuar con el ciclo
            raise StopIteration
    
    def sort_by_id(self):
        self.__particulas.sort()

    def sort_by_distancia(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)
    
    def sort_by_velocidad(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)

    def recorrido_profundidad_amplitud(self, origen):

        #Validar si el origen existe en el grafo
        if origen not in self.__grafo:
            return 0
        
        recorrido = 'Recorrido Profundidad:' + '\n' 
        profundidad = busqueda_profundidad(self.__grafo, origen)
        for vertice in profundidad:
            recorrido += str(vertice) + '\n'

        recorrido += '\n' + 'Recorrido Amplitud:' + '\n'
        amplitud = busqueda_amplitud(self.__grafo, origen)
        for vertice in amplitud:
            recorrido += str(vertice) + '\n'

        return recorrido

       

    
        
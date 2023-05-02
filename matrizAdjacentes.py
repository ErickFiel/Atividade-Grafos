"""
Iniciando nossa API, implemente representações computaciona de Grafos por meio de Listas de Adjacências e Matrizes de Adjacências.

Seguindo nossa API e a implementação computacional realizada na tarefa anterior, implemente uma classe Grafos que deve conter os sequintes métodos: 
a) V() retorna o número de vértices (feito)
b) A() retorna o número de arestas (feito) 
c) AddArestas() - Adiciona arestas (feito)
d) Adj() retorna arestas adjacentes (arestas que possuem vertices em comum)

"""

class Grafos:

    def __init__(self, vertices):
        #Inicializar uma matriz adjacente (N x N) inicial com todos os valores igual a 0
        self.vertices = vertices
        self.arestas = 0
        self.arestas_adjacentes = [[] for i in range (self.vertices)]
        self.grafo = [[0] * self.vertices for i in range(self.vertices)] 
    
    def V(self):
        return self.vertices

    def AddArestas(self, u, v):
        #Adicionar aresta no grafo
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1
        self.arestas_adjacentes[u].append((u,v))
        self.arestas_adjacentes[v].append((v,u))
        self.arestas += 1
    
    def Adj(self):
        return self.arestas_adjacentes

    def Printar_Grafo(self):
        print("Grafo:")
        for i in range(self.vertices):
            print(self.grafo[i])

grafo = Grafos(3)
grafo.AddArestas(0, 2)
grafo.Printar_Grafo()
print(grafo.Adj())    

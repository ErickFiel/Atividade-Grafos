

class Grafos:

    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = 0
        self.arestas_adjacentes = [[] for i in range(self.vertices)] 
        self.grafo = [[] for i in range(self.vertices)]

    def V(self):
        #Retorna o numero de vertices
        return self.vertices
    
    def A(self):
        #Retorna o numero de arestas
        return self.arestas

    def AddArestas(self, u, v):
        #Adiciona arestas no grafo
        self.grafo[u].append(v)
        self.grafo[v].append(u)
        self.arestas_adjacentes[u].append((u,v))
        self.arestas_adjacentes[v].append((v,u))
        self.arestas += 1
    
    def Adj(self):
        #Retorna a arestas adjacentes
        return self.arestas_adjacentes

    def Printar_Lista(self):
        #Mostrar a lista
        print("Lista Adjacente:")
        for i in range(self.vertices):
            print(f"Vertice {i}:", end = " ")
            for j in self.grafo[i]:
                print(f"{j} -> ", end = "")
            print("")

class Grafos:

    def __init__(self, vertices):
        #Inicializar uma matriz adjacente (N x N) inicial com todos os valores igual a 0
        self.vertices = vertices
        self.arestas = 0
        self.arestas_adjacentes = [[] for i in range (self.vertices)]
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        
        self.cor = [[] for i in range (self.vertices)]
        self.antecessor = [[] for i in range (self.vertices)]
        self.tempo = 0
        self.tempo_inicial = [[] for i in range (self.vertices)]
        self.tempo_final = [[] for i in range (self.vertices)]
        self.lista_DFS = [[] for i in range (self.vertices)]   
    
    def V(self):
        #Retorna o numero de vertices
        return self.vertices
    
    def A(self):
        #Retorna o numero de arestas
        return self.arestas

    def AddArestas(self, u, v):
        #Adicionar aresta no grafo
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1
        self.arestas_adjacentes[u].append((u,v))
        self.arestas_adjacentes[v].append((v,u))
        self.arestas += 1
    
    def Adj(self):
        #Retorna a arestas adjacentes
        return self.arestas_adjacentes  

    def Printar_Grafo(self):
        #Mostrar o grafo
        print("Grafo:")
        for i in range(self.vertices):
            print(self.grafo[i])

    def DFS_Visita(self, u):
        self.cor[u] = "CINZA"
        self.lista_DFS[u].append(u)
        self.tempo = self.tempo + 1
        self.tempo_inicial[u] = self.tempo
        for v in self.arestas_adjacentes[u]:
            if self.cor[u][v] == "BRANCO":
                self.antecessor[v] = u
                self.DFS_Visita(v)
        self.cor[u] = "PRETO"
        self.tempo_final[u] = self.tempo + 1 


    def DFS(self):
        for i in range(self.vertices):
            self.cor[i] = "BRANCO"
        for w in range(self.vertices):
            if self.cor[w] == "BRANCO":
                self.DFS_Visita(w)


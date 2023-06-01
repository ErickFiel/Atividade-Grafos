class Grafos:

    def __init__(self, vertices):
        #Informações do grafo
        self.vertices = vertices
        self.arestas = 0
        self.arestas_adjacentes = [[] for i in range(self.vertices)]
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        
        #Informações do DFS
        self.tempo = 0
        self.cor = [[] for i in range (self.vertices)]
        self.antecessor = [[None] for i in range (self.vertices)]
        self.tempo_inicial = [[] for i in range (self.vertices)]
        self.tempo_final = [[] for i in range (self.vertices)]
        self.lista_DFS = [[] for i in range (self.vertices)]   

        #Informações do BFS
        self.antecessorBFS = [None for i in range (self.vertices)]
        self.corBFS = [[] for i in range (self.vertices)]
        self.distancia = [[] for i in range (self.vertices)]
        self.filaQ = []
        
        #Relaxamento
        self.antecessorDij = [None for i in range (self.vertices)]
        self.d = [[] for i in range (self.vertices)]
        self.s = [] 
        self.filaDijkstra = [[] for i in range (self.vertices)] 
        
        #Floyd
        self.matrizFloyd = [None for i in range (self.vertices)] 
        self.antecessorFloyd = [None for i in range (self.vertices)]
    
    #Retorna o número de vértices
    def V(self):
        return self.vertices
    
    #Retorna o número de arestas
    def A(self):
        return self.arestas

    #Adicionar arestas no grafo
    def AddArestas(self, u, v):
        if u == v:
            if (u, v) in self.arestas_adjacentes[u]:
                print("Laço já existe.")
                return
            self.grafo[u][v] = 1
            self.arestas_adjacentes[u].append((u, v))
            self.arestas += 1
        else:
            if (u, v) in self.arestas_adjacentes[u] or (v, u) in self.arestas_adjacentes[u]:
                print("Aresta já existe.")
                return
            self.grafo[u][v] = 1
            self.grafo[v][u] = 1
            self.arestas_adjacentes[u].append((u, v))
            self.arestas_adjacentes[v].append((v, u))
            self.arestas += 1
    
    #Retorna a arestas adjacentes
    def Adj(self):
        return self.arestas_adjacentes  

    def printGrafo(self):
        #Mostrar o grafo
        print("Grafo:")
        for i in range(self.vertices):
            print(self.grafo[i])

    def DFS_Visita(self, u):
        #Será adicionadas as informações sobre o vértice
        self.cor[u] = "CINZA"
        self.lista_DFS[u].append(u)
        self.tempo = self.tempo + 1
        self.tempo_inicial[u] = self.tempo
        #Percorrer as arestas adjacentes
        for i in range(self.vertices):
            if self.grafo[u][i] == 1 and self.cor[i] == "BRANCO":
                self.antecessor[i] = u
                self.DFS_Visita(i)        
        self.cor[u] = "PRETO"
        self.tempo_final[u] = self.tempo + 1 

    def DFS(self):
        #Pintar todos os "vértices" de branco
        for i in range(self.vertices):
            self.cor[i] = "BRANCO"
        #Percorrer os "vértices" brancos
        for u in range(self.vertices):
            if self.cor[u] == "BRANCO":
                self.DFS_Visita(u)

    def BFS(self, fonte):
        for i in range(self.vertices):
            if fonte != i:
                self.corBFS[i] = "BRANCO"
                self.distancia[i] = "INDEFINIDO"
                self.antecessorBFS[i] = None
            else:
                self.corBFS[i] = "CINZA"
                self.distancia[fonte] = 0
                self.antecessorBFS[fonte] = None
        self.filaQ.append(fonte)
        while(len(self.filaQ) != 0):
            u = self.filaQ[-1]
            del self.filaQ[0]
            for w in range(self.vertices):
                if self.grafo[u][w] == 1 and self.corBFS[w] == "BRANCO":
                    self.corBFS[w] = "CINZA"
                    self.distancia[w] = self.distancia[u] + 1
                    self.antecessorBFS[w] = u
                    self.filaQ.append(w)
            self.corBFS[u] = "PRETO"

    def SingleSourse(self, s):
        for i in range(self.vertices):
            self.d[i] = float('inf')
            #self.antecessorDij[i] = None
        self.d[s] = 0
    
    def Relax(self, u, v):
        if self.d[v] > self.d[u] + self.grafo[u][v]:
            self.d[v] = self.d[u] + self.grafo[u][v]
            self.antecessorDij[v] = u
    
    def Dijkstra(self, s):
        self.SingleSourse(s)
        for i in range(self.vertices):
            self.filaDijkstra[i] = i
        while(self.filaDijkstra != []):
            u = self.filaDijkstra[0]
            del self.filaDijkstra[0]
            self.s.append(u)
            for i in range(self.vertices):
                if self.grafo[u][i] != 0:
                    self.Relax(u, i)  
    
    def BellmanFord(self, s):
        self.SingleSourse(self, s)
        for i in range(self.vertices - 1):
            for u, v in self.grafo:
                self.Relax(u, v)
        for u, v in self.grafo:
            if self.d[v] > self.d[u] + self.grafo[u][v]:
                return True
        return False

    def FloydWarshall(self):
        for v in range(self.vertices):
            for w in range(self.vertices):
                if v == w:
                    self.matrizFloyd[v][w] = 0
                self.matrizFloyd[v][w] = self.grafo[v][w]
        for k in range(self.vertices):
            for v in range(self.vertices):
                for w in range(self.vertices):
                    if (self.matrizFloyd[v][k] + self.matrizFloyd[k][w] < self.matrizFloyd[v][w]):
                        self.matrizFloyd[v][w] = self.matrizFloyd[v][k] + self.matrizFloyd[k][w]
                        self.antecessorFloyd[w] = k

    def ComponentesConectados(self):
        ListaComp = []
        for v in range(self.vertices):
            if not self.visitado[v]:
                componente = []
                self.DFS(v, componente)
                ListaComp.append(componente)
        return ListaComp               

    def printDFS(self):
        for i in range(self.vertices):
            print(f"| Ordem da lista -> {grafo.lista_DFS[i]} | Antecessor -> {grafo.antecessor[i]} | Tempo Inicial -> {grafo.tempo_inicial[i]} | Tempo Final -> {grafo.tempo_final[i]} |")
        print(f"Tempo Total -> {grafo.tempo}")   

    def printBFS(self):
        for i in range(self.vertices):
            print(f"Vertice --> {i} | Antecessor --> {self.antecessorBFS[i]} | Distancia --> {self.distancia[i]} |")
    
    def printDij(self):
        for i in range(self.vertices):
            print(self.s[i])

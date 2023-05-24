class Grafos:

    def __init__(self, vertices):
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
    
    def V(self):
        #Retorna o número de vertices
        return self.vertices
    
    def A(self):
        #Retorna o numero de arestas
        return self.arestas

    def AddArestas(self, u, v):
        #Adicionar aresta no grafo
        self.grafo[u][v] = 1
        self.grafo[v][u] = 1
        #Ajustar quando os vertices forem iguais
        self.arestas_adjacentes[u].append((u,v))
        self.arestas_adjacentes[v].append((v,u))
        self.arestas += 1
    
    def Adj(self):
        #Retorna a arestas adjacentes
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

    def printDFS(self):
        for i in range(self.vertices):
            print(f"| Ordem da lista -> {grafo.lista_DFS[i]} | Antecessor -> {grafo.antecessor[i]} | Tempo Inicial -> {grafo.tempo_inicial[i]} | Tempo Final -> {grafo.tempo_final[i]} |")
        print(f"Tempo Total -> {grafo.tempo}")   

    def printBFS(self):
        for i in range(self.vertices):
            print(f"Vertice --> {i} | Antecessor --> {self.antecessorBFS[i]} | Distancia --> {self.distancia[i]} |")

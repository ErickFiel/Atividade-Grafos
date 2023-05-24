
class Grafos:

    def __init__(self, vertices):
        #Informações do grafo
        self.vertices = vertices
        self.arestas = 0
        self.arestas_adjacentes = [[] for i in range(self.vertices)] 
        self.grafo = [[] for i in range(self.vertices)]
        self.lista_vertices = []
        #Informações do DFS
        self.tempo = 0
        self.cor = [[] for i in range (self.vertices)]
        self.antecessor = ["Ø" for i in range (self.vertices)]
        self.tempo_inicial = [[] for i in range (self.vertices)]
        self.tempo_final = [[] for i in range (self.vertices)]
        self.lista_DFS = [[] for i in range (self.vertices)] 
        #Informações do BFS
        self.antecessorBFS = ["Ø" for i in range (self.vertices)]
        self.corBFS = [[] for i in range (self.vertices)]
        self.distancia = [[] for i in range (self.vertices)]
        self.filaQ = []

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
        #Lista dos vértices
        if u not in self.lista_vertices:
            self.lista_vertices.append(u)
        if v not in self.lista_vertices:
            self.lista_vertices.append(v)
        
    
    def Adj(self):
        #Retorna a arestas adjacentes
        return self.arestas_adjacentes

    def printLista(self):
        #Mostrar a lista
        print("Lista Adjacente:")
        for i in range(self.vertices):
            print(f"Vertice {i}:", end = " ")
            for j in self.grafo[i]:
                print(f"{j} | ", end = "")
            print("")
    
    def printGrafo(self):
        #Mostrar o grafo
        print("Grafo:")
        for i in range(self.vertices):
            print(self.grafo[i])

    def DFS(self):
        #Pintar todos os "vértices" de branco
        for i in range(self.vertices):
            self.cor[i] = "BRANCO"
        #Percorrer os "vértices" brancos
        for u in range(self.vertices):
            if self.cor[u] == "BRANCO":
                self.DFS_Visita(u)

    def DFS_Visita(self, u):
        #Será adicionadas as informações sobre o vértice
        self.cor[u] = "CINZA"
        self.lista_DFS[u].append(u)
        self.tempo = self.tempo + 1
        self.tempo_inicial[u] = self.tempo
        #Percorrer as arestas adjacentes
        for i in range(len(self.grafo[u])):
            #Pegar a cor do vertice correspondente
            for w in range(len(self.lista_vertices)):
                if self.grafo[u][i] == self.lista_vertices[w]:
                    if self.cor[w] == "BRANCO":
                        self.antecessor[w] = u
                        self.DFS_Visita(w)   
        #Finaliza adicionando a cor "PRETO" ao vértice
        self.cor[u] = "PRETO"
        self.tempo_final[u] = self.tempo + 1 

    def BFS(self, fonte):
        #lista_vertices
        for i in range(self.vertices):
            if fonte != self.lista_vertices[i]:
                self.corBFS[i] = "BRANCO"
                self.distancia[i] = "INDEFINIDO"
                self.antecessorBFS[i] = "Ø"
            else:
                self.corBFS[i] = "CINZA"
                self.distancia[i] = 0
                self.antecessorBFS[i] = "Ø" 
        self.filaQ.append(fonte)
        while(len(self.filaQ) != 0):
            u = self.filaQ[-1]
            del self.filaQ[0]
            for w in range(self.vertices):
                if self.corBFS[w] == "BRANCO":
                    self.corBFS[w] = "CINZA"
                    self.distancia[w] = self.distancia[u] + 1
                    self.antecessorBFS[w] = u
                    self.filaQ.append(w)
            self.corBFS[u] = "PRETO"
    
    def printInformacaoDFS(self):
        for i in range(self.vertices):
            print(f"| Ordem da lista -> {grafo.lista_DFS[i]} | Antecessor -> {grafo.antecessor[i]} | Tempo Inicial -> {grafo.tempo_inicial[i]} | Tempo Final -> {grafo.tempo_final[i]} |")
        print(f"Tempo Total -> {grafo.tempo}")

    def printBFS(self):
        for i in range(self.vertices):
            print(f"Vertice --> {i} | Antecessor --> {self.antecessorBFS[i]} | Distancia --> {self.distancia[i]} |")
    
    def teste(self):
        print("")
        print(self.grafo[0])
    
    def testeLista(self):
        print(self.lista_vertices)

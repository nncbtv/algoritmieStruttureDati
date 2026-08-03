class Graph:
    
    def __init__(self, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def size(self):
        return len(self.matrix)

    def nodes(self): #Mi restittuisce una lista con tutti i nodi presenti nel grafo
        return [x for x in range(len(self.matrix))]

    def isEdge(self, i, j): #Controlla se esiste un arco tra i due nodi, self fiene passato in automatico non va messo quando lo chiami
        return self.matrix[i][j] == 1

    def insertEdge(self, i, j):
        n = len(self.matrix)
        if 0 <= i < n and 0 <= j < n:
            self.matrix[i][j] = 1

    def deleteEdge(self, i, j):
        n = len(self.matrix)
        if 0 <= i < n and 0 <= j < n:
            self.matrix[i][j] = 0
    
    #Inserisco una funzione fittizia per creare un grafo non orientato con una matrice di adiacenza
    def insertEdgeUndirected(self,x,y):
        self.insertEdge(x,y)
        self.insertEdge(y,x)
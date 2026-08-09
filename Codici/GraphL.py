class Graph:
    def __init__(self, n):
        """Crea un grafo vuoto con n nodi tramite liste di adiacenza."""
        self.adj = [[] for _ in range(n)] #Array di liste
        #Userò poi append e remove per gestire ogni lista normalmente

    def size(self):
        """Ritorna il numero di nodi."""
        return len(self.adj)

    def nodes(self):
        """Ritorna la lista dei nodi."""
        return [x for x in range(len(self.adj))]

    def insertEdge(self, x, y, peso): #Aggiungo il peso per rappresentare un grafo non orientato pesato
        """Inserisce un arco orientato da x a y se non esiste già."""
        if 0 <= x < len(self.adj) and 0 <= y < len(self.adj):
            for vicino, peso_esistente in self.adj[x]:
                if vicino == y:
                    return #Non lo aggiungo se già esiste, per il momento non acceto modifiche sul peso
            #Siccome non è orientato il collegamento deve esserci da entrambe le parti
            self.adj[x].append((y,peso))
            self.adj[y].append((x, peso))

    def deleteEdge(self, i, j):
        """Rimuove l'arco tra i e j se presente."""
        if 0 <= i < len(self.adj) and 0<= j < len(self.adj):
            for vicino, peso_esistente in self.adj[j]:
                if vicino == i: #Appena trovo l'arco lo rimuovo
                    self.adj[i].remove((j, peso_esistente))
                    self.adj[j].remove((i, peso_esistente))
                    return
        return

    def isEdge(self, i, j):
        """Verifica se esiste un arco tra i e j."""
        for vicino, peso in self.adj[i]:
            if vicino == j:
                return True
        return False

    def neighbors(self, i):
        """Ritorna i vicini del nodo i."""
        return list(self.adj[i])

    def outDegree(self, i): #Non serve se il grafo è non orientato
        """Grado di uscita del nodo i."""
        return len(self.adj[i])

    def inDegree(self, j): #Non serve se il grafo è non orientato
        """Grado di entrata del nodo j (scansione di tutte le liste)."""
        count = 0
        for neighbors_list in self.adj:
            if j in neighbors_list:
                count += 1
        return count

    def copy(self):
        """Ritorna una copia profonda del grafo."""
        new_g = Graph(len(self.adj))
        new_g.adj = [row[:] for row in self.adj]
        return new_g
#Alcune chiamate sono metodi primitivi che ha sul colab
def BFS(G,s): #Visita in ampiezza
    Queue = [s] #Inseirsco nella coda il nodo
    Visited = [] #Nodi del grafo visitati
    isVisited = [ False for _ in range(G.size())] #Inizialmente non ho visitato nessuno quindi tutto falso
    while Queue: #finchè ci sono nodi nella coda
        next = Queue.pop(0) #Prendo il nodo 
        if not isVisited[next]: #Controllo se non l'ho visitata
            Visited.append[next] #Aggiungo all vettore visita il nodo
            isVisited[next] = True #Metto a true per dire che l'ho visitato
            Adj = G.neighbors(next) #Prendo i vicini del nodo
            for x in Adj: #Se non li ho visitati li aggiungo alla coda
                if not isVisited[x]:
                    Queue.append(x)
    return Visited #ritorno i nodi visitati

#Visita in profondità
def DFS ( G, s):
    Queue = [s] #Inseirsco nella coda il nodo
    Visited = [] #Nodi del grafo visitati
    isVisited = [ False for _ in range(G.size())] #Inizialmente non ho visitato nessuno quindi tutto falso
    while Queue: #finchè ci sono nodi nella coda
        next = Queue.pop() #Prendo il nodo dalla coda con politica lifo
        if not isVisited[next]: #Controllo se non l'ho visitata
            Visited.append[next] #Aggiungo all vettore visita il nodo
            isVisited[next] = True #Metto a true per dire che l'ho visitato
            Adj = G.neighbors(next) #Prendo i vicini del nodo
            for x in Adj: #Se non li ho visitati li aggiungo alla coda
                if not isVisited[x]:
                    Queue.append(x)
    return Visited #ritorno i nodi visitati

def DFSRec( G, s ):
    Visited = [ s ] #S è il primo nodo ad essere visto
    DFSRec2 ( G, s, Visited )
    return Visited

#Questo metodo esplora un cammino
def DFSRec2( G, x, Visited ):
    Adj = G.neighbors(x) #Trovo i vicini
    for y in Adj: #Itero su di loro e li aggiungo se non ho visitato uno di loro
        if not y in Visited: #Se l'ho visitato non chiamo la ricorsione su quel nodo
            Visited.append(y)
            DFSRec2( G, y, Visited ) #Se non l'ho visto continuo a trovare e scendere nei vicini dello stesso nodo ricorsivamente
    
#Comincio con importare le primitive per il grafico
from Codici.GraphL import Graph
import math
G = Graph(5) #creo il grafico

def neighbors(G, nodo): #Devo creare una funzione che mi ritorna in una lista i vicini del mio nodo
    #Comincio con il preparare la lista risulante
    nodiVicini = [] #Dovrà avere come componenti [nodoVicino, peso]
    nodiGrafo = G.nodes() #Prendo i nodi del grafo
    for nodoSelezionato in nodiGrafo: #Comincio lo scorrimento dei nodi del grafo
        if G.isEdge(nodo, nodoSelezionato): #Se esiste l'arco tra i due nodi, matrice costa O(1) mentre O(n) nel caso peggiore delle liste di adiacenza
            peso = G.getWeight(nodo, nodoSelezionato) #Prendo il peso dell'arco
            nodiVicini.append([nodoSelezionato, peso]) #Lo aggiungo alla lista dei vicini
    return nodiVicini #Ritorno la lista a fine funzione
'''
STUDIO COMPLESSITÀ TEMPORALE
Devo principalmente scorrere la lista dei nodi presenti nel grafo e controllare se esiste un arco che crea connessione con il nodo passato, la velocità dipende da come
viene implementata la struttura del grafo, nel caso peggiore il nodo ha come vicini tutti gli altri quindi O(n) nel caso in cui è implementato a matrice.
Nel caso in cui abbiamo un implementazione con le liste di adiacenza dobbiamo scorrere dentro la lista dei vicini di ognuno n volte con un costo di ricerca nel caso peggiore di o(n)
la complessità peggiora fino a O(n^2) poiché nella lista adiacenza potrei avere un nodo al centro con tutti i nodi vicini
STUDIO COMPLESSITÀ SPAZIALE
La mia funzione costruisce una lista grande quanto sono i nodi vicini al nodo passato che nel caso peggiore possono essere tutti gli altri nodi del grafo, O(n)
'''

def isConnected(G): #Devo controllare se G ha tutti i nodi connessi tra di loro, con una visita in ampiezza BFS (Breadth-First Search), controllo per ogni nodo gli archi uscenti
    nodiGrafo = G.nodes() #Prendo la lista dei nodi del grafo
    nodiVisitati = [ False for i in range (G.size())] #tengo conto di quale nodi ho visitato
    nodiVisitati[0] = True #Parto con la visita dell'albero dal primo nodo
    coda = [] #Coda dei nodi da visitare
    coda.append(nodiGrafo[0]) #Inserisco il nodo di partenza
    while len(coda) > 0: #Finché ci sono nodi da visitare
        nodoCorrente = coda.pop(0) #Prendo un nodo dalla coda
        #Comincio a controllare i vicini del nodo preso se sono raggiungibili
        for nodoVicino, pesoVicino in neighbors(G, nodoCorrente):
            if not nodiVisitati[nodoVicino]: #Se non ho visitato il vicino lo visito e lo metto in lista per visitarlo al prossimo giro
                nodiVisitati[nodoVicino] = True
                coda.append(nodoVicino)
    for nodo in nodiGrafo:
        if not nodiVisitati[nodo]: #Se un nodo non è stato visitato do errore
            return False
    return True #Se ho visitato tutti i nodi ho verificato che il grafo è connesso
'''
STUDIO COMPLESSITÀ TEMPORALE
sostanzialmente dipende dalla visita in ampiezza cioè O(n+m) dove n sono i nodi e m gli archi, nel caso di un implementazione con le liste di adiacenza nel caso peggiore
abbiamo una lista dei vicini pari ad n quindi O(n^2). Con la matrice per ogni nodo devo controllare n posizioni per verificare se esiste un arco allora o(n^2)
STUDIO COMPLESSITÀ SPAZIALE
Se prendo in considerazione solo lo spazio utilizzato senza quello del grafo O(n) giusto lo spazio per il vettore e la coda.
Se prendo in considerazione anche il grafo con le liste di adiacenza ottengo O(n+m) dove m sono gli archi verso i vicini, cioè le liste dei vicni nella lsita di adiacenza
Se prendo in considerazione anche il grafo con la matrice O(n^2) poiché la matrice occupa già O(n^2) per rappresentare il grafo
'''

def boundedDegreeNetwork(G, d): #Scompongo un grafo in cui i nodi hanno tra di loro massimo d archi
    if not isConnected(G): #Controllo se è connesso
        return None
    #Mi servono tutti gli archi in ordine crescente
    nodiGrafo = G.nodes()
    archi = []
    for nodo in nodiGrafo:
        for nodoVicino, pesoVicino in neighbors(G, nodo):
            if nodo<nodoVicino: #cosi non inserisco due volte lo stesso arco
                archi.append([nodo, nodoVicino, pesoVicino])
    #Devo ordinare gli archi in modo crescente
    archi.sort(key=lambda arco: arco[2]) #Definsico che devo ordinarli per il peso con una funzione lambda, cioè per ogni array prendi il 3 campo
    gradi = [0 for x in nodiGrafo] #Ogni nodo deve avere al massimo d archi selezionati
    archiSelezionati = [] #Vettore di ritorno della funzione
    parent = [x for x in nodiGrafo] #Inizialmente trattiamo ogni nodo come una componente separata, ogni indice indica un nodo, il valore a quale nodo è connesso
    def find(x): #Funzione che mi trova a quale nodo sono collegato cosi da non creare un ciclo con altri archi
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y): #Per unire due nodi tra di loro nel vettore parent
        radiceX = find(x)
        radiceY = find(y)

        if radiceX != radiceY:
            parent[radiceY] = radiceX
    
    for x, y, peso in archi: #Scorriamo gli archi ordinati
        if gradi[x] >= d or gradi[y] >= d: #Se uno  dei due nodi ha raggiunto il numero massimo di archi lo scarto
            continue
        if find(x) == find(y): #Se sono collegati già tramite un altro nodo non ne aggiungo un altro perché creo un ciclo
            continue
        #superati i controlli aggiungo l'arco e aumento il numero degli arichi per i nodi
        archiSelezionati.append([x, y, peso])

        gradi[x] += 1
        gradi[y] += 1

        union(x, y)
        
    return archiSelezionati

'''
STUDIO COMPLESSITÀ TEMPORALE
chiamiamo per prima cosa isConnected con complessità O(n+m)
chiamo neighbors n volte con costo O(n) => O(n^2)
Poi kruskal mi occupa O(m*n) nel caso peggiore diventa m=n e tutto si riduce a O(n^3)
STUDIO COMPLESSITÀ SPAZIALE
Se prendo in considerazione solo lo spazio utilizzato senza quello del grafo O(n) giusto lo spazio per il vettore e la coda.
Se prendo in considerazione anche il grafo con le liste di adiacenza ottengo O(n+m) dove m sono gli archi verso i vicini, cioè le liste dei vicni nella lsita di adiacenza
Se prendo in considerazione anche il grafo con la matrice O(n^2) poiché la matrice occupa già O(n^2) per rappresentare il grafo
'''
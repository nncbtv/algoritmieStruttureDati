from Codici.GraphL import Graph #Importo la libreria per le primitive
import math #Mi serve per usare i suoi metodi

def neighbors(G, nodo): #Deve restituire i vicini del nodo passato
    nodiGrafo = G.nodes() #Prendo la lista di nodi dal grafo con la primitiva apposita passata dalla traccia
    nodiVicini = [] #Lista dei nodi vicini al nodo passato, da riempire
    for nodoGrafo in nodiGrafo:
        if G.isEdge(nodo, nodoGrafo): #Siccome non è orientato posso direttamte fare in questo modo
            nodiVicini.append([nodoGrafo, G.getWeight(nodo, nodoGrafo)]) #Coppia [nodo, peso arco per arrivarci]
    return nodiVicini #ritorno la lista dei vicini
'''
STUDIO COMPLESSITÀ TEMPORALE
La nostra funzione scorre tutti i nodi del grafo per controllare poi se esiste un arco con il nodo passato, O(n).
In base però a come è implementato il nostro grafo concretamente questa complessità cambia, se implementato con una matrice di adiacenza O(1) per controllare gli archi n volte => O(n).
Con una lista di adicenza nel peggiore dei casi O(n^2) posso avere una lista di adiacenza di un nodo con tutti gli n nodi dentro, tutti sono suoi vicini
STUDIO COMPLESSITÀ SPAZIALE
Lo spazio ausiliario utilizzato è il vettore dei vicini che nel peggiore dei casi può avere O(n) elementi
'''
def costruisciCapcità(grafo): #Deve restituire una matrice in cui gli indici sono i nodi e il valore delle celle la capienza dell'arco che li collega
    n = grafo.size() #Prendo il numero di nodi presenti nel grafo
    matriceCapacita = [[ 0 for _ in range(n)] for _ in range (n)] #Creo una matrice n*n con capacità iniziale tutta zero
    #Cominciamo a scorrere i nodi per aggiornare le capacità della matrice
    nodiGrafo = grafo.nodes() #Lista dei nodi presenti nel grafo
    for nodoSelezionato in nodiGrafo:
        #Prendo ogni nodo e controllo i suoi vicini
        for nodoVicino, pesoArco in neighbors(grafo, nodoSelezionato): #Scorrimento lista vicini, [nodoVicino, pesoArco] funzione scritta prima
            matriceCapacita[nodoSelezionato][nodoVicino] = pesoArco #Aggiorno la capacità dell'arco che collega i due nodi
            #Se l'arco non esiste resta zero e soddisfa la proprietà passata dalla traccia, se un arco non esiste deve esserci zero nella cella della matrice
    return matriceCapacita #Ritorno la matrice capacità con le capacità massime degli archi
'''
STUDIO COMPLESSITÀ TEMPORALE
La nostra funzione crea la matrice e la riempie scorrendo i nodi del grafo e gli archi.
Lo scorrimento dei nodi mi costa O(n), all'interno dell ciclo chiamiamo la nostra funzione neighbors scritta in precedenza con costo O(n).
La complessità temporale di questa funzione tende a O(n^2)
Se però il nostro grafo viene implementato direttamente con una matrice di adiacenza posso ridare subito la matrice finendo con O(1)
STUDIO COMPLESSITÀ SPAZIALE
Creiamo una matrice O(n*n) oltre allo spazio utilizzato dal grafo, e la lista di nodi da scorrere.
Tende quindi a O(n^2)
'''
def movimentazioneMax(G, S, T): #Usando la matrice creata precedentemente dobbiamo trovare il percorso che ci permette di spostare più merce da S verso T problema di maxflow
    n = G.size() #Numero di nodi del grafo
    capArchi = costruisciCapcità(G) #Costruisco per prima cosa la matrice su cui lavaorare
    #Devo svolgere una visita BFS nel grafo e capire quanto flusso massimo inviare sugli archi
    flussoTotale = 0 #Capacità totale del grafo
    nodiCammino, flussoCammino = trovaCammino(G, capArchi, S, T) #Cerco il primo percorso da analizzare
    while flussoCammino > 0:
        flussoTotale += flussoCammino #Aggiorno il flusso totale inserendo quello massimo per il cammino trovato
        #Ora per i prossimi cammini le capacità degli archi cambiano, consumo con il flusso il cammino passato
        nodo = T #Comincio a scorrere i nodi del cammino al contrario per aggiornare il flusso restante sugli archi
        while nodo != S:
            nodoPrecedente = nodiCammino[nodo] #Prendo il nodo precedente, alla prima iterazione quello precedente a T
            capArchi[nodoPrecedente][nodo] -= flussoCammino #Consumo con il flusso l'arco verso il nodo
            capArchi[nodo][nodoPrecedente] += flussoCammino #Aggiungo flusso entrante al nodo
            nodo = nodoPrecedente #Passo il nodo precedente per tornare a ritroso
        #Una volta aggiornati gli archi cerco un altro cammino
        nodiCammino, flussoCammino = trovaCammino(G, capArchi, S, T) #Cerco un altro percorso da analizzare
    return flussoTotale #Finiti i percorsi ritono il flusso totale del grafo
    
    
def trovaCammino(G, capArchi, S, T): #Trova un cammino da S a T
    nodiVisitati = [False]*G.size() #Perché devo tenere conto dei nodi che ho già visitato
    nodiVisitati[S] = True #Perché S è il nodo di partenza
    predecessori = [None]*G.size() #Mi servono i predecessori per poi poter ricostruire il cammino
    coda = [(S, math.inf())] #Metto i nodi in coda per visitare poi i loro vicini ed arrivare a T visitando in BFS
    flussoCammino = -1 #Il flusso massimo di un arco con capacità minima, -1 non ha trovato cammini
    while len(coda) > 0:
        nodoAttuale, massimoMerce = coda.pop(0) #Prendo i nodi in ordine FIFO
        if nodoAttuale == T:
            flussoCammino = massimoMerce #Prendo il flusso del cammino
            break #Sono già arrivato a destinazione
        for nodoVicino in range (G.size()): #Scorro la lista dei vicini, senza usare la funzione neighbors
            if capArchi[nodoAttuale][nodoVicino] > 0: #Esiste un collegamento tra i due nodi, sono vicini e la loro capacità è maggiore di zero
                if not nodiVisitati[nodoVicino]: #Se non ho visitato il nodo posso andarci
                    nodiVisitati[nodoVicino] = True #Marco il nodo come visitato
                    predecessori[nodoVicino] = nodoAttuale #Aggancio il predecessore da cui provengo
                    massimoMerceVicino = min(massimoMerce, capArchi[nodoAttuale][nodoVicino]) #Aggiorno il massimo con l'arco più piccolo
                    coda.append([nodoVicino, massimoMerceVicino]) #Metto in coda il vicino per poi esplorare i suoi vicini
    return predecessori, flussoCammino #Ritorno il cammino
'''
STUDIO COMPLESSITÀ TEMPORALE
La creazione della matrice costa O(n^2) come visto in precedenza.
Il nostro ciclo while nel peggiore dei casi viene eseguito O(m) volte perché ogni iterazione satura un arco, al  suo interno chiamimo la funzione per trovare un cammino con visita BFS
di costo O(n^2) perché scorre tutti i nodi e controlla i suoi vicini con la matrice scorrendoli tutti di nuovo per ognuno di essi.
Generalmente questa funzione costa O(m*n^2) per un grafo non orientao m=n^2 che porta tutto a O(n^4)
STUDIO COMPLESSITÀ SPAZIALE
Sono principalemnte vettori di al più O(n) ma la matrice creata domina con O(n^2)
'''
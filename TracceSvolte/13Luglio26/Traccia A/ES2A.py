from Codici.GraphL import Graph
#Per semplificare l'esercizio adotto un implementazione del grafo con liste di adiacenza

G = Graph(5) #Creo il grafo

def neighbors(G, x):
    ris = [] #Lsita vuota incui inserisco il risultato
    listaNodi = G.nodes() #Lista di tutti i nodi del grafo
    for nodo in listaNodi: #Comincio a scorrere i nodi del grafo
        if (G.isEdge(nodo, x)): #Controllo se esiste un arco tra i due nodi
            peso = G.getWeight(nodo, x) #Prendo il peso dell'arco
            ris.append([nodo, peso]) #Lo aggiungo alla lista
    return ris #Ritorno il risultato

'''

STUDIO COMPLESSITÀ
Siccome dobbiamo chiamare la lista dei nodi del grafo e poi scorrerla abbiamo una complessità di O(n)
Nel caso peggiore quando controllo se è presente un arco è possibile che vengano scansionati nuovamente tutti i nodi,
questo porta il tutto ad un complessità totale di O(n^2) dove n è il numero di nodi dell grafo
Per la complessità spaziale abbiamo massimo O(n)

'''


def coloraComponente( G, s, colori ):
    #Creo prima di tutto una coda per implementare la visita in ampiezza del grafo
    coda = []
    coda.append(s) #Aggiungo in coda il nodo di partenza
    #Comincio ad assegnare un colore arbitrario a S per poi aggiornare la lista
    colori[s] = 0
    #Cominciamo a scorrere i suoi nodi vicini per colorarli
    while len(coda) > 0: #Finché ho nodi da esplorare
        nodoCorrente = coda.pop(0) #Prendo il nodo inserito per primo per garantire FIFO
        for nodoVicino, _ in neighbors(G, nodoCorrente): #Uso per convenzione _ significa che l'altro valore non mi interessa, in questo caso il peso
            if ( colori[nodoVicino] == -1 ):
                colori[nodoVicino] = 1 - colori[nodoCorrente] #Modifico il colore del nodo
                coda.append(nodoVicino) #Aggiungo il nodo in coda per poi controllare dopo i suoi vicini
           
            if ( colori[nodoCorrente] == colori[nodoVicino] ): #Controllo se entrambi hanno lo stesso colore
                return False #Errore nella colorazione
    return True

'''
STUDIO COMPLESSITÀ
Per tutti i nodi chiamiamo la funzione precedente quindi nel caso peggiore O(n^3)
Per la complessità spaziale abbiamo massimo O(n)

'''

    
def isBipartite(G):
    colori = [ -1 for x in G.nodes()] #Creo il vettore dei nodi colorati per sapere a quale squadra appartengono
    squadra0 = []
    squadra1 = []
    for nodo in G.nodes(): #Scorro i nodi per colorarli se non sono stati colorati
        if colori[nodo] == -1: #Se il nodo non è stato ccolorato provo a colorarlo
            if (not coloraComponente(G, nodo, colori)):
                return (False, None) #Se la funzione di colorazione mi da false significa che cè un ciclo e non è bipartito
    for nodo in G.nodes(): #Ora ricreo le squadre con la lista dei nodi
        if ( colori[nodo] == 0): #Per ogni colore di nodo lo sistemo nella propria squadra
            squadra0.append(nodo)
        else:
            squadra1.append(nodo)
    return (True, [squadra0, squadra1])

'''
STUDIO COMPLESSITÀ
Sempre nel caso peggiore abbiamo O(n^3) poiché chiamiamo per ogni nodo la funzione precedente anche qui
Per la complessità spaziale abbiamo massimo O(n)
'''

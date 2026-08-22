#Scrivo al volo le primitive per non avere errori nell'ide
def createTree(): #Restituisce un albero vuoto
    return []

def addNode(infoNodo): #Aggiunta nodo foglia
    return [infoNodo, [],[]]

def insert(A, x): #Inserisce un nodo nell'albero A, suppongo sia un ABR anche se la traccia non ce lo dice
    if (info(A) == info(x) ): return #I valori nell'albero devono essere distinti quindi non lo aggiungo
    if (isNull(A)): return addNode(x) #Se l'albero è vuoto inserisco il primo nodo
    if info(A) > info(x):
        A[1] = insert(left(A),x) #Sposto l'inserimento verso sx
    else:
        A[2] = insert(right(A),x) #Sposto l'inserimento a dx

def left(A): #Restituisce sotto albero sx
    return A[1]

def right(A): #Restituisce sotto albero dx
    return A[2]

def info(A): #Restituisce il valore della radice
    return A[0]

def setInfo(A, x): #Imposta il valore della radice
    A[0] = x

def isNull(A): #Controlla se l'albero è vuoto
    return A==[]

def pathBalance(albero, k):
    if isNull(albero):
        return False #L'albero non deve essere vuoto, per forza h>=1
    return esploraAlbero(albero, k, 0, False) #Faccio scendere nell'albero una funzione ausiliaria

def esploraAlbero(albero, k, somma, precedenteNegativo):
    if info(albero)<0 and precedenteNegativo:
        return False #Ho trovato due negativi consecutivi
    nuovaSomma = somma + info(albero) #Sommo le radici su cui sono passato, cioè i nodi
    if ( isNull(left(albero)) and isNull(right(albero)) ): #Sono arrivato ad una foglia e controllo se questo cammino va bene con le condizioni della traccia
        if ( nuovaSomma%k == 0):
            return True
        else:
            return False
    return esploraAlbero(left(albero),nuovaSomma, info(albero)<0) or esploraAlbero(right(albero), nuovaSomma, info(albero)<0) #Procedo a scendere a sx e dx nell'albero, appena un ramo mi da true esco

'''
STUDIO COMPLESSITÀ TEMPORALE
CASO MIGLIORE
La funzione termina subito poiché la radice è direttamente una foglia quindi O(1).
Anche se però l'albero è enorme non siamo costretti ad esplorare tutt i cammini, ce ne basta uno solo per uscire grazie all'or della funzione esploraAlbero.
CASO PEGGIORE
Dobbiamo scorrere tutti i nodi dell'albero quindi abbiamo O(n) dove n sono i nodi, questo è dovuto al fatto che dobbiamo partire dalla radice per arrivare a tutti i nodi foglia e controllarli

STUDIO COMPLESSITÀ SPAZIALE
CASO MIGLIORE
Sempre O(1) per gli stessi motivi
CASO PEGGIORE
Devo arrivare dalla radice ad una foglia e poi si chiudono tutte le chiamate a cascata, O(h) dove h è l'altezza dell'albero, se degenera tutto l'albero in una lista O(n) dove n sono i nodi

CASO ALBERO ABR
Non stiamo cercando un valore specifico nell'albero quindi temporalmente le caratteristiche di un ABR non ci aiutano lato temporale e la complessità è identica
Nella complessità spaziale migliora soltanto se l'albero è bilanciato portando la complessità a O(log n) poiché per ogni livello dell'albero i nodi raddoppiano e l'altezza si trova con log n
'''
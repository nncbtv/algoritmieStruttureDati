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

def pathRange (albero, Z1, Z2): 
    #Devo trovare un cammino dalla radice ad una foglia,
    #dove ogni nodo deve avere il valore compreso tra i due range e la sequenza deve essere crescente
    #Comincio a scendere nell'albero in modo ricorsivo cercando la soluzione
    return discesaAlbero(albero, Z1, Z2, None)

def discesaAlbero(albero, E1, E2, nodoPrecedente):
    if (isNull(albero)): return False #Alebro Vuoto
    #Comincio con il verificare le condizioni
    if not (E1<=info(albero)<=E2):
        return False #Il valore non è compreso nell'intervallo quindi do lo stop per violazione prima condizione
    if nodoPrecedente is not None: #Se il nodo precedente passato non è vuoto lo controllo
        if ( info(albero)<nodoPrecedente):
            return False #La sequenza è decrescente tra due nodi quindi non va bene
    if (isNull(left(albero)) and isNull(right(albero))):
        return True #Significa che se sono arrivato qui rispetto tutte le condizioni della traccia con questo cammino
    if (isNull(left(albero))):
        #Scorro l'albero sulla destra
        return discesaAlbero(right(albero), E1, E2, info(albero))
    if (isNull(right(albero))):
        #Scorro l'albero sulla sx
        return discesaAlbero(left(albero), E1, E2, info(albero))
    #Controllo l'albero che ha due figli scendendo in entrambe le direzioni
    return discesaAlbero(left(albero), E1, E2, info(albero)) or discesaAlbero(right(albero), E1, E2, info(albero))

'''
STUDIO COMPLESSITÀ TEMPORALE
Nel caso migliore la radice è già una foglia e rispetta le condizioni della traccia oppure violo subito una delle condizioni quindi finiamo con O(1)
Nel caso peggiore la funzione esplora tutti i cammini passando per tutti i nodi con O(n)
Quando invece viene esplorato un solo cammino e termino ho una complessità pari all'altezza dell'albero O(h)

STUDIO COMPLESSITÀ SPAZIALE
Nel caso migliore O(1) perché facciamo soltanto una chiamata a funzione oltre quella già avviata
Nel caso peggiore chiamiamo tante funzioni fino ad arrivare ad una foglia O(h) dove h è l'altezza dell'albero, se è bilanciato O(log n) se degenera o(n)

STUDIO IN CASO DI ABR
Non stiamo cercando un valore specifico nell'albero però possiamo capire in quale sezione dell'albero scendere, se a sx oppure a dx con le proprietà dell'abr tagliando
tutti i nodi che cadono in un intervallo più piccolo o maggiore di quello dato e portando ad una ricerca più mnirata ma nel caso peggiore rimaniamo sempre a O(n) potremmo
avere ad esempio un intervallo molto largo che ci porta ad esplorare tutti i cammini dell'albero, quindi asintoticamente restano pressoché le stesse complessità
'''
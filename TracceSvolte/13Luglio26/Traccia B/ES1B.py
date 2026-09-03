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

def isSymmetric(A): #Questa funzione mi restituisce True se l'albero è simmetrico
    if isNull(A):
        return True #Un albero vuoto è sicuramente simmetrico
    if isNull(left(A)) and isNull(right(A)):
        return True #Un albero con un solo nodo è simmetrico
    return simmetria(left(A), right(A)) #Chiamata alla funzione ricorsiva ausiliaria

def simmetria(albero1, albero2):
    if isNull(albero1) and isNull(albero2):
        return True #sono arrivato senza problemi alle foglie
    if isNull(albero1) or isNull(albero2):
        return False #Albero sbilanciato
    if info(albero1) != info(albero2):
        return False #Non hanno lo stesso valore nella stessa posizione
    return simmetria(left(albero1), left(albero2)) and simmetria (right(albero1), right(albero2)) #Controllo ricorsivamente la simmetria, in and mi basta uno falso per terminare
'''
STUDIO COMPLESSITÀ TEMPORALE
La nostra funzione nel migliore dei casi termina subito entrando nei primi due if con costo O(1).
Nel peggiore dei casi esploriamo tutti i cammini dell'albero controllando per ogni nodo se vengono soddisfatte le proprietà di simmetria, quindi O(n).
Dobbiamo per forza scorrere tutti i nodi, non ci basta trovare un solo percorso valido, dobbiamo controllare tuttol'albero.
STUDIO COMPLESSITÀ SPAZIALE
Lo stack si riempie nel migliore dei casi di una sola chiamata a funzione, senza entrare nelle ricorsioni con costo O(1).
Nel peggiore dei casi lo stack chiuderà a cascata le chiamate appena arriva ad una foglia, quindi O(h) cioè l'altezza dell'albero, il percorso più lungo da radice a foglia
APPUNTO BST
In questo caso non cambia nulla poiché dobbiamo sempre esplorare il nostro albero controllando le proprietà per ogni nodo e non stiamo cercando un valore usando le proprietà del BST.
'''

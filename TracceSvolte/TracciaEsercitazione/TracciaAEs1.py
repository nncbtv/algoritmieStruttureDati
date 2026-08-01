#TRACCIA A ESERCITAZIONE

#ESERCIZIO 1

#Funzioni date dalla traccia e aggiunte per testing
def createTree(): #Restituisce un albero vuoto, definito come tupla [valore, FiglioSinistro, FiglioDestra]
    return []

def isNull(A): #Controllo se vuoto
    return A == []

#Funzioni per il ritorno dei valori

def info(A): #Valore radice
    return A[0] if not isNull(A) else None

def left(A): #Figliosx
    return A[1] if not isNull(A) else []

def right(A): #Figliodx
    return A[2] if not isNull(A) else []

def setInfo(A, x): #Modifico il valore radice
    if not isNull(A): 
        A[0] = x

# Aggiunta nodo foglia - crea un nuovo nodo con valore x
def addNode(x):
    return [x, [], []]

def insert(A, x): #Inserimento di un figlio
    if isNull(A):
        return addNode(x)
    if x < A[0]:
        A[1] = insert(A[1], x)
    else:
        A[2] = insert(A[2], x)
    return A

#Funzione richiesta da implementare nella traccia
def checkTree(A, z1, z2):
    if isNull(A): return False #Non posso chiamare la funzione su un albero vuoto
    if z1>=z2: return False #Se inserisco i dati errati esco direttamente
    if isNull(left(A)) and isNull(right(A)): return False #Sono in una foglia, non posso accettare questo nodo come B
    #Da questo punto in poi ho già un nodo candidato B poiché esso non è foglia di A, ciò significa che il nodo a sua volta contiene dei figli
    #Eseguo il controllo della condizione supponendo di trovarmi su B dato che ho già controllato che il nodo possa rappresentarlo
    def checkB( sottoAlberoDx, z1, z2, b ): #Funzione che  mi controlla il sottoalbero e verifica la condizione
        if isNull(sottoAlberoDx): return False #Posso finire in un albero vuoto quando chiamo ricorsivamente
        #Per prima cosa devo vedere se il sottoalbero passato ha figli foglia
        if isNull( left(sottoAlberoDx)) and isNull(right(sottoAlberoDx) ): #Se il sotto albero passato non ha figli sono su una foglia e controllo il criterio
            return z1<=b+info(sottoAlberoDx)<=z2
        else: #continuo a scendere
            return checkB(left(sottoAlberoDx),z1,z2,b) and checkB(right(sottoAlberoDx),z1,z2,b) #continuo a scendere
        
    if checkB( right(A), z1, z2, info(A) ): #Se trovo un b Valido ho finito
        return True
    else:
        return checkTree( left(A), z1, z2) or checkTree(right(A), z1, z2) #continuo a scansionare l'albero
    
"""
STUDIO DELLA COMPLESSITÀ ALGORITMICA

L'algoritmo principalmente per trovare un nodo b valido deve esplorare tutto l'albero e poi il sotto albero dx del nodo candidato b fino ad arrivare alle foglie 
e verificare la condizione.
Nel caso peggiore, un albero sblianciato verso dx ci porta a controllare per ogni nodo candidato b i suoi sotto alberi potando la complessità a O(n^2) poichè per ogni
nodo va controllato il suo sottoalbero ma essendo sbilanciato li controlla tutti.
Nel caso migliore posso avere un albero costituito da 3 nodi e trovarlo subito avendo complessità O(1)

"""
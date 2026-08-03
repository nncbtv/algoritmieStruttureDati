#Comincio con lo scrivere le funzioni standard per il mio nuovo albero

def ABST(): #Ritorna un nuovo albero O(1)
    return []

def empty(A): #Controlla se vuoto O(1)
    return A == []

def key(A): #Ritorno la chiave O(1)
    if not empty(A):
        return A[0]
    else:
        return []
    
def value(A): #Ritorno il valore del nodo O(1)
    return A[1] if not empty(A) else []

def height(A): #Ritorno l'altezza del nodo O(1)
    return A[2] if not empty(A) else -1
#È la distanza che c'è tra un nodo e la sua foglia più lontana
#Metto -1 se è vuoto per non rompere i metodi di confronto dopo con il max

def getSum(A): #Ritorno la somma del sottoalbero O(1)
    return A[3] if not empty(A) else []

def left(A): #Ritorno il figlio sx del nodo O(1)
    return A[4] if not empty(A) else []

def right(A): #Ritorno il figlio dx del nodo O(1)
    return A[5] if not empty(A) else []

def setLeft(A, x): #Attacco un nuovo figlio O(1)
    A[4] = x

def setRight(A, x): #Attacco un nuovo figlio O(1)
    A[5] = x

def setHeight(A, x): #Imposto la nuova altezza O(1)
    A[2] = x

def updateHeight(A): #Aggirono l'altezza O(1)
    return 1+max( height(left(A)), height(right(A)) )

def setSum(A, x): #Imposto la somma O(1)
    A[3] = x
    
def updateSum(A): #Calcolo la nuova somma O(1)
    return value(A)+getSum(left(A))+getSum(right(A))

def addNode(k, v): #Aggiunta nodo foglia O(1)
    #Mi passano chiave e valore, l'altezza è zero, non ha figli
    #La somma del suo sottoalbero coincide con il proprio valore poiché è una foglia
    return [k, v, 0, v, [], []]

def insert (A, k, v):

    if empty(A): 
        return addNode(k, v) #Se l'albero è vuoto inserisco una foglia
    
    if key(A) == k: #Se trovo la stessa chiave non faccio nulla, non possono esistere due chiavi identiche
        return A
    
    #Se l'albero contiene nodi devo trovare il posto in cui metterlo
    #Controlliamo se va nel sottoalbero destro o sinistro per prima cosa
    if (k>key(A)):
        #Qui il nodo deve entrare nel sottoalbero dx
        setRight(A, insert( right(A), k, v ) ) #scendo ricorsivamente
        #Una volta sceso a cascata le chiamate verrano chiuse e aggiorno i valori
        setHeight( A, updateHeight(A) )
        setSum ( A, updateSum(A) )
    else:
        #Qui il nodo deve entrare nel sottoalbero sx
        setLeft(A, insert ( left(A), k, v ) ) #scendo ricorsivamente
        #Una volta sceso a cascata le chiamate verrano chiuse e aggiorno i valori
        setHeight( A, updateHeight(A) )
        setSum ( A, updateSum(A) )

    """
        COMPLESSITÀ INSERIMENTO

        Per inseirre un nodo nel nostro albero dobbiamo prima trovare la sua posizione esplorando un cammino che ci porta ad una foglia
        Durante la risalita verranno aggiornati tutti i campi di ogni nodo ma essedno una operazione costante si riduce tutto a O(1)
        La parte complessa sta nel trovare il cammino, se l'albero è vuoto lo troviamo subito quindi O(1) opure viene inserito direttamente
        Nel caso medio esploreremo l'albero bilanciato fino ad arrivare ad una sua foglia, quindi per la ricerca binaria O(log n) dove n sono i nodi
        Nel caso peggiore un albero degenera in una lista e dobbiamo scorrerlo tutto O(n)
    """


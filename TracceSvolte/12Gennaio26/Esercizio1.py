#Comincio con lo scrivere le funzioni standard per il mio nuovo albero.
#ho impostato la struttura dati nel seguente modo: [key, value, height, sum, [figliosx], [figliodx]]

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
    return A[3] if not empty(A) else 0

def left(A): #Ritorno il figlio sx del nodo O(1)
    return A[4] if not empty(A) else []

def right(A): #Ritorno il figlio dx del nodo O(1)
    return A[5] if not empty(A) else []

def setKey(A, x): #Aggiorno la chiave O(1)
    A[0] = x

def setValue (A, x):
    A[1] = x
    
def setLeft(A, x): #Attacco un nuovo figlio O(1)
    A[4] = x

def setRight(A, x): #Attacco un nuovo figlio O(1)
    A[5] = x

def setHeight(A, x): #Imposto la nuova altezza O(1)
    A[2] = x

def updateHeight(A): #Aggiorno l'altezza O(1)
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
    else:
        #Qui il nodo deve entrare nel sottoalbero sx
        setLeft(A, insert ( left(A), k, v ) ) #scendo ricorsivamente
    setHeight( A, updateHeight(A) )
    setSum ( A, updateSum(A) )
    return A #Ritorno il nuovo albero

    """
        COMPLESSITÀ INSERIMENTO

        Per inserire un nodo nel nostro albero dobbiamo prima trovare la sua posizione esplorando un cammino che ci porta ad una foglia
        Durante la risalita verranno aggiornati tutti i campi di ogni nodo ma essendo una operazione costante si riduce tutto a O(1)
        La parte complessa sta nel trovare il cammino, se l'albero è vuoto lo troviamo subito quindi O(1) opure viene inserito direttamente
        Nel caso medio esploreremo l'albero bilanciato fino ad arrivare ad una sua foglia, quindi per la ricerca binaria O(log n) dove n sono i nodi
        Nel caso peggiore un albero degenera in una lista e dobbiamo scorrerlo tutto O(n) dove n sono sempre i nodi
    """

def minimo ( albero ): #Migliore O(1) peggiore O(h) dove h è l'altezza dell'albero
    if ( empty( albero ) ):
        return None #Albero passato vuoto
    if ( empty ( left( albero ) ) ): #Se non ho valori minori alla chiave essa è il minimo
        return albero #Restituisco l'albero poiché mi serve chiave e valore
    else:
        return minimo ( left ( albero ) ) #Scendo ancora sulla sinistra
    
def delete( albero, chiave ):
    if empty(albero): 
        return albero #la chiave passata non esisteva
    #comincio a scorrere l'albero per capire dove si trova il nodo
    if ( chiave > key(albero) ):
        setRight( albero, delete ( right(albero), chiave ) ) #Mi sposto sul sottoalbero DX se c'è, se vuoto lo catturo col primo if
        setHeight( albero, updateHeight(albero) ) #Resetto l'altezza
        setSum( albero, updateSum( albero ) ) #Aggiorno la somma
    elif ( chiave < key( albero ) ):
        setLeft( albero, delete ( left(albero), chiave ) ) #Mi sposto sul sottoalbero SX se c'è, se vuoto lo catturo col primo if
        setHeight( albero, updateHeight(albero) ) #Resetto l'altezza
        setSum( albero, updateSum( albero ) ) #Aggiorno la somma
    else: #nodo trovato chiave == key ( albero )
        #Qui deve partire la cancellazione del nodo
        if ( empty( left( albero ) ) and empty( right( albero ) ) ): #Era un nodo foglia, posso eliminarlo direttamente
            return []
        elif ( empty( left( albero ) ) ): #Se ho solo il figlio dx passo quello e mi elimino come nodo
            return right( albero )
        elif ( empty ( right ( albero ) ) ):#Se ho solo il figlio sx passo quello e mi elimino come nodo
            return left( albero )
        else:#Se il nostro nodo ha due figli verrà rimpiazzato da quello più piccolo sulla dx per tenere le proprietà del BST
            minDx = minimo ( right ( albero ) ) #Trovo il minimo destro
            setKey ( albero, key( minDx ) ) #Prenderò il minimo del sottoalbero dx e lo collego al mio posto
            setValue ( albero, value ( minDx ) )
            setRight ( albero, delete ( right( albero ), key( minDx ) ) ) #Tolgo il minDx dalla posizione in cui era
            #Aggiorno i valori
            setHeight(albero, updateHeight(albero))
            setSum(albero, updateSum(albero))
    return albero #Ritorno il nuovo albero

'''
    STUDIO COMPLESSITÀ
    La cancellazione dipende dall'altezza dell'albero, poiche dobbiamo muoverci in esso per trovare il nodo e sostituirlo, quindi O(h) dove h è l'altezza.
    I valori aggiuntivi non peggiorano la complessità dato che si aggiornano automaticamente ad ogni chiusura delle chaimate ricorsive con O(1).
    Quindi caso migliore O(1), bilanciato O(log n) e peggiore O(n) dove n indicano i nodi
'''

def prefix_sum(albero, chiave):
    #Siccome devo sommare i valori di tutti i nodi con chiave <= di quella passata posso ottimizzare il tutto usando il campo sum del sottoalbero che si crea quando la chiave passata è minore dell'albero che sto considerando
    if empty( albero ):
        return 0
    somma = 0 #Inizializzo una variabile somma da restituire poi a fine metodo
    if ( key (albero) <= chiave ):
        somma = value(albero) + somma + getSum (left( albero )) #Sicuramente tutto questo sottoalbero ha chiavi più piccole
        somma = somma + prefix_sum ( right ( albero ), chiave) #Vado a dx, potrebbe esserci una chaive uguale o più piccola più avanti nell'albero
        return somma
    else:
        return prefix_sum ( left(albero), chiave ) #Scendo a sx per trovare una chiave più piccola
'''

    STUDIO COMPLESSITÀ
    Siccome possiamo utilizzare il campo sum dei nodi nel caso migliore abbiamo O(1), la parte destra dell'albero non esisste, non ci sono chiavi maggiori
    Nel caso medio dobbiamo visitare un cammino dalla radice fino ad uno stop che può essere una foglia, quindi coincide con l'altezza dell'albero a cui arriviamo O(h)
    Nel peggiore dei casi l'albero è sbilanciato verso destra e lo scorriamo tutto, quindi O(n)
    Ovviamente e l'albero è bialnciato avremo O(log n)

'''
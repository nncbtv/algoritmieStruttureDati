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

def lca(A, x, y):
    #Non so se A è un ABR quindi ho valori sparsi in cui cercare
    if (isNull(A)): return #Sono arrivato ad una foglia/albero vuoto, non dovrei arrivarci perchè x e y sono presenti in A
    if ( info(A) == x or info(A) == y):
        return info(A) #Ho trovato uno dei due nodi
    #Scendo a sx e dx nell'albero per cercare i nodi
    sinistra = lca(left(A), x, y)
    destra = lca(right(A), x, y)
    #Appena la ricorsione torna da me io sono il lca poichè hanno trovato x e y sotto di me
    if ( sinistra == x or sinistra == y ): #Controllo se la sinsitra che mi è stata passata da sotto è corretta
        if (destra == x or destra ==y ): #Controllo se la destra passata è corretta
            return info(A) #LCA trovato
        else:
            return sinistra #Ritorno la sx alla chiamata superiore a me
    else:
        return destra #Ritorno la destra passata da sotto alla chiamata superiore
    #sostanzialmnete scendo per trovare x e y e poi risalgo finché non li ho tutti e due per dire che sono lca
    
#Supponiamo ora di avere un BST, in questo modo il problema di semplifica perché sappiamo in quale direzione esplorare l'albero
def lcaBST(A, x, y):
    if ( info (A) == x or info(A) == y ): return info(A) #Ho trovato uno dei due nodi, oppure uno dei due nodi è l'antenato stesso
    #Controllo con le proprietà del BST il posto in cui devo andare a cercare
    if ( info(A)>x and info(A)>y ): 
        return lcaBST(left(A), x, y) #Mi sposto sulla sinistra se i valori sono minori della radice
    elif ( info(A)<x and info(A)<y ): 
        return lcaBST(right(A), x, y) #Mi sposto sulla destra se i valori sono maggiori della radice
    else: #Potrei essere nel punto in cui uno dei due è maggiore e l'altro minore quindi ho trovato il lca
        #Per definizione ne x e ne y devo contenersi nel sotto albero dx o sx del nodo lca, questa proprietà è garantita dal BST
        return info(A)
    
'''
STUDIO COMPLESSITÀ
Prima parte in cui non abbiamo BST:
Dobbiamo per forza scorrere tutto l'albero e quindi tutti i nodi finché non troviamo x e y, quindi O(h) dove h è l'altezza dell'albero per la complessità spaziale, se l'albero degenera in una lista
scorriamo tutti i nodi quindi O(n) dove n sono i nodi nel caso peggiore, nel caso migliore ci fermiamo al primo if quindi O(1)
Seconda parte con un albero BST:
Sostanzialmente lo spazio è identico, O(h) dove h è l'altezza dell'albero mentre per la ricerca scendiamo nel peggiore dei casi a O(n) dove n sono i nodi dell'albero degenerato in una lista
Nel caso medio O(log n) per la ricerca binaria se è bilanciato
Stessa cosa caso migliore in cui usciamo con O(1)
'''
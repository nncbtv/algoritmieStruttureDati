def albero(): #L'albero parte da una lista vuota fino ad avere tuple annidate in cui avrò [radice, figliosx, figliodx]
    return []

def alberoVuoto(albero): #Passato un albero controllo se è vuoto
    return albero == []

def figliosx(albero): #Passato un albero restituisce il suo figlio sx
    return albero[1]

def figliodx(albero): #passato un albero restituisce il suo figlio dx
    return albero[2]

def presente(albero, nodo): #resistuisce true se il nodo è presente nella tupla
    if alberoVuoto(albero): return False #Controllo se mi stanno passando un albero vuoto, se vero sicuramente non c'è il nodo
    if albero[0] == nodo: return True #Se il nodo corrisponde con la radice allora l'ho trovato
    return presente(albero[1], nodo) or presente(albero[2], nodo) #Ricerco ricorsivamente prima nel sottoalbero sx e poi in quello dx

def creanodo(nodo): #Creo un nodo senza figli
    return [ nodo, [], [] ]

def inserisciNodo( albero, nodo ):
    #Controllo se il valore è già nell'albero, non faccio nulla se è true
    if presente(albero, nodo): 
        print(f"Il nodo: {nodo} è già presente nell'albero")
        return None
    if alberoVuoto(albero): #Controllo se l'albero è vuoto oppure no, in caso sia vuoto sto creando il primo nodo
        return creanodo(nodo)
    if nodo<=albero[0]: #Controllo se va messo a sx
        albero[1] = inserisciNodo(albero[1], nodo) #Scendo sul sottoalbero sx
    else: #Se non va a sx va sicuro a dx
        albero[2] = inserisciNodo(albero[2], nodo) #Scendo sul sottoalbero dx
    return albero #Ritorno l'albero con il nuovo nodo

def ricerca(albero, nodo): #Cerco un nodo nell'albero
    if alberoVuoto(albero): return False #Se mi passano un albero vuoto do falso, stessa cosa se arrivo alle foglie e non l'ho trovato ancora
    if albero[0] == nodo: return True #Se corrisponde alla radice l'ho trovato
    if nodo > albero[0]: return ricerca(albero[2], nodo) #Se il nodo è maggiore della radice mi sposto nel sottoalbero dx
    else: return ricerca(albero[1], nodo) #Nel sottoalbero sx altrimenti
    
#Da questo commento in poi cominciano i metodi di bilancio

def trovaMinimo(albero): #Cerco il minimo in un albero
    if alberoVuoto(albero[1]): return albero[0] #Se sono arrivato ad un foglia restituisco la sua radice
    else: return trovaMinimo(figliosx(albero)) #Scendo verso sx nell'albero

def bilancio(albero): #Funzione che calcola il bilancio dell'albero
    return contaLivello(figliosx(albero))-contaLivello(figliodx(albero))  #Comincio il calcolo del bilancio dopo aver ottenuto i risultati dai metodi ricorsivi

def contaLivello(albero):
    if alberoVuoto(albero): return 0 #Un albero vuoto non ha livelli
    if not alberoVuoto(figliosx(albero)): return 1+contaLivello(figliosx(albero)) #Se l'albero ha un figliosx procedo in quella direzione
    if not alberoVuoto(figliodx(albero)): return 1+contaLivello(figliodx(albero)) #Se l'albero ha un figliodx procedo in quella direzione
    return 0 #Se non ho figli vuol dire che sono in una foglia quindi do 0 alle foglie

def altezza(albero):
    return contaLivello(albero) +1 #Siccome quando conto i livelli omettendo la radice in questo caso la conto


#Da questo punto in poi cominciano le visite dell'albero

def visitaInOrder(albero): #visita sinistro->radice->destro
    if alberoVuoto(albero): return [] #Un albero vuoto non ha nulla da visitare
    l = [] #Lista vuota per la visita
    #Questo metodo ricorsivo comincia a scendere a sx dell'albero e poi risale man mano aggiungendo la radice quando non abbiamo più filgi
    def inOrderRec(nodo): #Annido una funzione
        if not alberoVuoto(nodo): #Controllo se il nodo passato non è vuoto
            inOrderRec(nodo[1]) #Passo il nodo figlio sx
            l.append(nodo[0]) #Aggiungo la radice
            inOrderRec(nodo[2]) #Passo il nodo figlio dx
    inOrderRec(albero) #Chiamo la funzione annidata per cominciare ad aggiungere i nodi alla lista di visita
    return l #Ritorno la lista (In pratica i valori sono in ordine crescente)

def visitaPreOrder(albero): #visita radice->sinistro->destro
    if alberoVuoto(albero): return [] #Un albero vuoto non ha nulla da visitare
    l = [] #Lista vuota per la visita
    #Aggiungo il nodo radice e dopodichè comincio a scorrere l'albero verso sinistra e risalendo aggiungo i figlidx
    def preOrderRec(nodo): #Funzione ricorsiva annidata
        if not alberoVuoto(nodo): #Controllo prima di tutto se il nodo è non vuoto
            l.append(nodo[0])  #Aggiungo il nodo alla lista
            preOrderRec(nodo[1]) #Scorro i suoi figlisx
            preOrderRec(nodo[2]) #Scorro i suoi figlidx
    preOrderRec(albero) #Chiamo la funzione annidata sull'albero
    return l #Ritorno la lista (Copio esattamente com'è l'albero)

def visitaPostOrder(albero): #visita sinistro->destro->radice
    if alberoVuoto(albero): return [] #Un albero vuoto non ha nulla da visitare
    l = [] #Lista vuota per la visita
    def postOrderRec(nodo): #Funzione ricorsiva annidata per scorrere l'albero
        if not alberoVuoto(nodo): #Controllo se il nodo non è vuoto
            postOrderRec(nodo[1]) #Scorro i suoi figlisx
            postOrderRec(nodo[2]) #Scorro i suoi figlidx
            l.append(nodo[0]) #Aggiungo la radice
    postOrderRec(albero) #Chiamo la funzione ricorsiva sull'albero
    return l #Ritorno la lista (Usta comunemente per eliminare la'labero)


def eliminazione(albero, nodo): #eliminazione di un nodo dall'albero
    if alberoVuoto(albero): return #Se l'albero è vuoto faccio direttamente il return
    if nodo>albero[0]: #Se il nodo è maggiore della radice mi sposto nel sotto albero dx
        albero[2] = eliminazione(albero[2], nodo)
        return albero
    elif nodo<albero[0]: #Se il nodo è minore uguale della radice mi sposto nel sotto albero sx
        albero[1] = eliminazione(albero[1], nodo)
        return albero
    if alberoVuoto(figliosx(albero)) and alberoVuoto(figliodx(albero)): #Caso 1: Nodo foglia ingloba anche il caso sia radice
        albero = [] #Tolgo tutti i figli vuoti creando una lista
        return albero
    elif alberoVuoto(figliosx(albero)) and not alberoVuoto(figliodx(albero)): #Caso 2-A: Ho il figlio DX
        albero = figliodx(albero) #Ritorno al padre il nuovo puntatore al figlio sotto il nodo da eliminare
        return albero
    elif not alberoVuoto(figliosx(albero)) and alberoVuoto(figliodx(albero)): #Caso 2-B: Ho il figlio SX
        albero = figliosx(albero) #Ritorno al padre del nodo attuale da eliminare il suo figlio sx
        return albero
    else: #Caso 3: Ho entrambi i figli quindi sostituisco con il suo successore in-order (minimo del sotto albero DX)
        temp = trovaMinimo(figliodx(albero))
        albero[0] = temp #Minimo del sottoalbero DX
        albero[2] = eliminazione(albero[2], temp) #Cancello ora il minimo dall nuovo albero
        return albero
        
#Sopra questo commento il codice funziona, sotto da sistemare
"""
Funzione lasciata come esercizio: Restituisce la somma dei valori associati a tutte le chiavi minori o uguali a k. 
L’algoritmo deve sfruttare il campo sum e non deve visitare inutilmente l’intero albero.
"""
def prefix_sum(albero, k):
    if (alberoVuoto(albero)): return 0 #Se l'albero è vuoto ritorno 0, non influisce nella somma
    if (albero[0]>k): return prefix_sum(figliosx(albero), k) #Se la radice è maggiore di k mi sposto sull'albero sx
    else: return prefix_sum(figliosx(albero),k)+prefix_sum(figliodx(albero), k) #Se il nodo attuale è minore di k, faccio la somma e mi sposto nel suo sottoalbero, prima sx e poi dx

"""
Funzione Lasciata come esercizio: Restituisce la massima somma di valori ottenibile lungo un cammino che parte dalla radice e termina in una foglia.
"""
def max_weight_path(albero):
    if (alberoVuoto(albero)): return 0 #Se l'albero è vuoto non c'è nessun cammino
    if (alberoVuoto(figliodx(albero))) and (alberoVuoto(figliosx(albero))): return albero[0] #Sono arrivato ad una foglia il valore è il nodo stesso
    if (alberoVuoto(figliodx(albero))) and not (alberoVuoto(figliosx(albero))): return albero[0]+max_weight_path(figliodx(albero)) #Se ho solo il figlio dx scendo in quel sotto albero
    if not (alberoVuoto(figliodx(albero))) and (alberoVuoto(figliosx(albero))):  return albero[0]+max_weight_path(figliosx(albero)) #Se ho il figlio sx scendo in quel sotto albero
    return albero[0]+max_weight_path(figliodx(albero))+max_weight_path(figliosx(albero)) #Se ho entrambi i figli scendo in entrambi

"""
Funzione lasciata per casa: Restituisce la somma di valori contenuti in nodi fino al livello k (incluso)
"""
def sum_liv_k(albero, k):
    if (alberoVuoto(albero)): return 0 #Se l'albero è vuoto non ho livelli da sommare
    if (k == 1 ): #Sono arrivato all'ultimo livello Partendo da n fino ad n-1
        return 0 #Non occore sommare nulla qui dato che ho già fatto tutto nel return 
    return albero[0]+sum_liv_k(figliosx(albero), k-1)+sum_liv_k(figliodx(albero), k-1) #Prendo la radice e mi sposto nei sottoalberi

"""
Funzione lasciata per casa: dati due alberi A e B, restituisca True se l’albero A `e sottoalbero dell’albero B, False atrimenti
"""
def sub(alberoA, alberoB):
    if (alberoVuoto(figliosx(alberoA)) and alberoVuoto(figliodx(alberoA))): return False #Sono arrivato ad una foglia quindi non ho trovato nulla di simile
    if (alberoA[0] == alberoB[0]): #Qui potrebbe cominciare un sottoalbero perché le radici sono uguali
        if (figliosx(alberoA) == figliosx(alberoA) and figliodx(alberoA) == figliosx(alberoB)): #Se anche i loro figli sono uguali ho trovato un sottoalbero
            return True
    if (figliosx(alberoA) == alberoB[0]): return sub(figliosx(alberoA), alberoB) #Se la radice è uguale a mio figlio lo cerco l'albero b nel sottoalbero figliosx di alberoA
    if (figliodx(alberoA) == alberoB[0]): return sub(figliodx(alberoA), alberoB) #Se la radice del figlio mio dx è uguale alla radice dell'albero b potrebbe essere li e lo cerco
    if (alberoA[0]<alberoB[0]): return sub(figliodx(alberoA), alberoB) #mi sposto sul sottoalbero dx
    return sub(figliosx(alberoA), alberoB) #mi sposto sul sottoalbero sx

"""Funzione lasciata come esercizio: Estrerre tutti i nodi a distanza h dalla radice"""
def pop_liv(albero, h):
    l = [] #Lista in cui inserisco i nodi da estrarre
    def pop_liv_rec(albero, altezza): #Funzione ricorsiva annidata che scende negli alberi sx e dx fino a distanza h
        pop_liv_rec(figliosx(albero), h-1) #Scendo di un livello a sx
        pop_liv_rec(figliodx(albero), h-1) #Scendo di un livello a dx
        if ( altezza == 1 ): #Raggiunta la distanza h aggiungo le radici alla lista
            l.append(albero[0])
    pop_liv_rec(albero, h) #Chiamo la funzione ricorsiva
    return l #Lista delle chiavi estratte fino a livello h

#Provare a creare un albero bilanciato AVL

tupla = [5, 2, 3, 6, 1]
Tree = albero()
for x in tupla:
    Tree = inserisciNodo(Tree, x)
    print(f"Sto inserendo: {x} in {Tree}")
min = trovaMinimo(Tree)
print(f"Il minimo nell'albero è: {min}")
bilanciato = bilancio(Tree)
print(f"Il bilanciamento dell'albero dalla radice è: {bilanciato}")
h = altezza(Tree)
print(f"Altezza albero: {h}")
numero = 6
#print(f"Sto cercando il nodo {numero}, risultato: {ricerca(Tree, numero)}")
print(f"La visita in-order dell'albero è: {visitaInOrder(Tree)}")
#print(f"La visita pre-order dell'albero è: {visitaPreOrder(Tree)}")
#print(f"La visita post-order dell'albero è: {visitaPostOrder(Tree)}")
Tree = eliminazione(Tree, numero)
print(f"Eliminazione: {numero} dall'albero: {Tree}")
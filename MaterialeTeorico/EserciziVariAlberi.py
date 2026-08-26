#In questo file mettiamo esercizi di vario tipo sugli alberi
#Importo le primitive degli alberi per poterle usare
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

def esisteCammino(A, k):
    #Devo trovare un cammino radice-foglia senza negativi la cui somma di nodi è uguale a k
    if (isNull(A)):
        return False #Caso principale in cui non ha senso continuare
    return discesaAlbero(A, k, 0) #Chiamata a funzione ricorsiva per poter scorrere l'albero e trovare il cammino

def discesaAlbero( A, k, somma ):
    if isNull(A):
        return False #Mi hanno passato un figlio che non esiste
    #Controllo se un nodo è positivo prima di prenderlo in considerazione
    if ( info(A) <= 0 ): return False #Non posso accettare un cammino con nodi non positivi, tolgo anche lo zero per evidenziare che voglio solo numeri strettamente positivi
    #Se il nodo è positivo posso aggiungerlo alla somma
    somma = somma + info(A)
    #Qui posso controllare le condizioni del caso base per l'uscita dalla ricorsione
    if ( isNull(left(A)) and isNull(right(A)) ): #Sono arrivato a fine cammino
        if ( somma == k ): #Controllo se il cammino ha una somma cumulativa valida
            return True
        else:
            return False
    #Continuo a scendere nell'albero, l'or mi ferma al primo cammino valido, nel peggiore dei casi esploro tutti gli altri
    return discesaAlbero( left(A), k, somma ) or discesaAlbero( right(A), k, somma )

'''
STUDIO COMPLESSITÀ TEMPORALE
Cominciamo con il studiare i diversi casi in cui il nostro algoritmo termina:
Caso migliore: l'albero è vuoto terminiamo subito senza nemmeno avviare ricorsione O(1), ci fermiamo alla chiamata di esiste cammino
Caso peggiore: l'albero è sbilanciato e degenera in una lista in cui scorriamo tutti i nodi O(n) oppure scorriamo tutti i cammini

STUDIO COMPLESSITÀ SPAZIALE
Si somigliano molto con la complessità temporale:
Caso migliore: O(1) una sola chiamata alla prima funzione
Caso peggiore: O(h) poiché dobbiamo esplorare tutti i nodi di un cammino, O(log n) se l'albero è bilanciato
'''

def pathMaxSum(albero, valoreSomma):
    #Devo trovare un cammino in cui ho almeno un negativo, la somma di tutto il cammino deve essere uguale a valoreSomma e soprattuto non deve contenere due numeri pari consecutivi
    if (isNull(albero)): return False #Caso base
    return discesaRicorsiva(albero, valoreSomma, 0, None, False) #Chiamata alla funzione che scenderà nell'albero

def discesaRicorsiva(albero, k, somma, nodoPrecedente, presenteNegativo):
    #Comincio con il controllare le condioni di uscita
    if isNull(albero):
        return False #Mi hanno passato un figlio che non esiste
    if not (nodoPrecedente is None): #Prima di tutto controllo se ho un precedente
        if (nodoPrecedente%2==0 and info(albero)%2 == 0):
            return False #Ho trovato due pari consecutivi
    if not presenteNegativo:
        presenteNegativo = info(albero) < 0 #Aggiorno la presenza di un negativo se non ne avevo trovato ancora uno
    #Qui posso aggiornare la somma che mi sto portando dietro dalla ricorsione poiché il cammino è ancora valido
    somma = somma + info(albero)
    #Adesso devo controllare se il mio cammino è valido altrimenti va tagliato
    if (isNull(left(albero)) and isNull(right(albero))): #Se sono arrivato ad un foglia controllo le condizioni del cammino per dare True
        if presenteNegativo: #Deve avere per forza almeno un negativo
            if somma == k: #La somma deve essere uguale al valore passato
                return True
            else:
                return False #La somma ha valore diverso
        else:
            return False #Non ha un negativo
    else:
        return discesaRicorsiva( left(albero),k,somma,info(albero),presenteNegativo ) or discesaRicorsiva( right(albero),k,somma,info(albero),presenteNegativo ) #Non ero ad una foglia
#COMPLESSITÀ IDENTICA ALLA FUNZIONE PRECEDENTE

#Ora provo ad implementare un esercizio con visita BFS (Visita in ampiezza dell'albero)
def livelloMinimo(albero, k):
    #Ritorna il livello del nodo che ha valore k, -1 se non trova nulla
    if isNull(albero): return -1
    #Per prima cosa devo prendere un nodo e scansionare i suoi figli per poi avanzare di livello, questo per qualsiasi nodo
    coda = []
    coda.append([albero, 0]) #Inserisco per prima cosa la radice con livello zero
    #Comincio a scorrere i figli dei nodi presenti in coda 
    while len(coda) > 0:
        #Prendiamo il nodo e il livello attuale per capire se coincide con quello cercato
        nodo, livello = coda.pop(0)
        #Controllo se è quello corretto e ritorno il livello uscendo dalla funzione
        if ( nodo == k): return livello
        #Ora se il nodo non è quello corretto comincio a scorre in ampiezza, aggiungo alla coda i figli del nodo preso in considerazione attualmente
        if not isNull(left(nodo)):
            coda.append([left(nodo), livello+1]) #Aggiungo prima il sinistro perché la visita in ampiezza va da sx a dx, il figlio si troverà al livello sottostante
        if not isNull(right(nodo)):
            coda.append([right(nodo), livello+1]) #Aggiungo dopodiché il dx
    #Finita la visita se non ho trovato nulla comunico:
    return -1

'''
STUDIO COMPLESSITÀ TEMPORALE
Supponiamo di avere una coda con estrazione e inserimento pari a O(1), magari una coda a doppia estremità.
Nel caso migliore terminiamo con O(1) perché k potrebbe essere proprio la radice.
Nel caso peggiore la visita si svolge su tutto l'albero senza trovare nulla, quindi scorrendo tutti i nodi una volta soltanto O(n)
STUDIO COMPLESSITÀ SPAZIALE
In questo caso diversamente dalla DFS non abbiamo chiamate ricorsive che occupano nello stack spazio pari ad h ma soltanto il numero di nodi da visitare, cioè un intero livello al massimo
Nel caso migliore: O(1) un nodo ha un solo figlio
Nel caso peggiore: O(n) asintoticamente concettualmente potrai avere se l'albero è bilanciato l'ultimo livello delle foglie tutte pieno pari a n/2 che asintoticamente è n
meglio ancora definire O(w) dove w è la massima larghezza dell'albero
'''

def sommaLivello(albero, livello):
    #Visitando l'albero in modo BSF appena arrivo al livello passato faccio la somma di tutti i nodi
    if isNull(albero): return -1
    #Setup struttura ausiliaria per BFS
    nodiDaVisitare = []
    nodiDaVisitare.append([albero, 0])
    sommaLivello = 0
    while len(nodiDaVisitare) > 0: #Avvio BFS, si ferma dopo aver sommato i nodi di tutto il livello
        nodo, livelloNodo = nodiDaVisitare.pop(0)
        if livelloNodo == livello:
            sommaLivello = sommaLivello + info(nodo) #Sommo i nodi del livello togliendoli dalla coda fino ad esaurirli e uscire dal while
        else: #Scendo di un livello, ancora non sono al livello desiderato
            if not isNull(left(nodo)):
                nodiDaVisitare.append([left(nodo), livelloNodo+1])
            if not isNull(right(nodo)):
                nodiDaVisitare.append([right(nodo), livelloNodo+1])
    return sommaLivello

'''
STUDIO COMPLESSITÀ TEMPORALE
Supponendo sempre di avere una lista il cui inserimento e estrazione pari a O(1):
Nel caso migliore: O(1) perché dobbiamo sommare il primo livello ad esempio
Nel caso peggiore: O(n) dobbiamo arrivare ad esmepio al livello foglie quindi abbiamo visitato tutti i nodi dell'albero
STUDIO COMPLESSITÀ SPAZIALE
Supponendo sempre di avere una lista il cui inserimento e estrazione pari a O(1):
Nel caso migliore: dobbiamo solamente sommare la radice O(1)
Nel caso peggiore: O(w) dove w sono i numeri di nodi in un livello che coincide con O(n) asintoticamente
'''

#IMPLEMENTAZIONE BFS RICORSIVA
'''
Generalemente non si implementa ricorsivamente ma per allenamento proviamo a farla poiché è una cosa interessante. La ricorsione ci aiuta nell'automatizzare le 
operazioni ma non riesce da sola a gestire una coda FIFO necessaria per la visita BFS quindi dobbiamo passargliela e far lavorare la potenza della ricorsione su di essa
'''
#Qui prima di chiamare la funzione faremo:
#codaNodi = [albero] per passare l'albero e visitarlo nelle sue parti
def BFSRec(codaNodi):
    if codaNodi == 0:
        return #Ho finito la visita
    nodo = codaNodi.pop(0) #Prendo il nodo dalla lista
    print(info(nodo)) #Elaboro le info del nodo, stampa fittizia epr simulare altre operazioni
    #Aggiunta figli alla lista
    if not isNull(left(nodo)):
        codaNodi.append(left(nodo))
    if not isNull(right(nodo)):
        codaNodi.append(right(nodo))
    return BFSRec(codaNodi) #richiamo ricorsivamente

'''
STUDIO COMPLESSITÀ TEMPORALE
Ogni nodo viene visitato almeno una volta O(n)
STUDIO COMPLESSITÀ SPAZIALE
La coda può contenere n nodi O(n)

Sostanzialmente non abbiamo ottenuto un vantaggio con questa implementazione e quindi è quasi inutile aggiugnere complessità di scrittura e continuare ad usare il tipo
non ricorsivo per essere più leggibili
'''
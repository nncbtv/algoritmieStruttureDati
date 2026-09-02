#Importo la libreria per gestire le primitive dei grafi
from Codici.GraphL import Graph
import heapq #Per gestire priority queue
import math #Per impostare a infinito i valori delle celle dei vettori

G = Graph(5) #Grafo fittizio con 5 nodi

def neighbors(G, nodo): #Supponendo non sia orientato
    nodiGrafo = G.nodes() #Mi prendo i nodi presenti nel grafo con una primitiva
    nodiVicini = [] #Lista dei vicini al nodo passato
    #Comincio a scorrere i nodi per capire se sono vicini al nodo passato
    for nodoSelezionato in nodiGrafo:
        if (G.isEdge(nodo, nodoSelezionato)):
            nodiVicini.append(nodoSelezionato) #Qui aggiungo anche il peso dell'arco se è un grafo pesato
    return nodiVicini #Ritorno la lista dei vicini al nodo passato
'''
STUDIO COMPLESSITÀ TEMPORALE
In base a come è implementato il nostro grafo la complessità può cambiare, generalmente il ciclo for scorrerà sempre tutti i nodi del grafo quindi O(n)
il punto critico è controllare se esiste un arco, G.isEdge quindi dipende dall'implementazione, per matrice di adiacenza è immediato poichè devo solo controllare
un cella di una matrice O(1). COMPLESSITÀ CON MATRICE: O(n)
Invece con una lista di adiacenza il discorso cambia poiché per ogni nodo devo scorrere una lista di vicini che potenzialmente potrebbe avere tutti gli n nodi se 
ad esempio il nodo passato sta al centro ed abbiamo un collegamento tipo a stella portando la funzione a O(n^2).
STUDIO COMPLESSITÀ SPAZIALE
Restituiamo una lista che al massimo può contenere tutti i nodi del grafo, quindi O(n) anche G.nodes() restituisce una lista O(n)
ATTENZIONE
Ricordo che l'implementazione sopra scritta non dipende dal tipo di implementazione del grafo, poiché se sapessimo a priori che il grafo è implementato con le liste di
adiacenza potremmo restituire direttamente la lista dei vicini del nodo per come è strutturata l'implementazione stessa
'''
def raggiungibileBFS(G, s, t): #Devo trovare un percorso da S a T in un grafo non orientato e non pesato, True se esiste e False altrimenti
    #Ho implementato la visita BFS per risolvere, usa una coda FIFO per visitare il grafo in ampiezza
    if ( s == t ): return True
    nodiVisitati = [False] * G.size() #Siccome potrei entrare in un ciclo non visito lo stesso nodo due volte
    nodiVisitati[s] = True #Per non tornare su me stesso
    codaVicini = [s] #Metto in coda i nodi per visitare i loro vicini in ordine FIFO
    while len( codaVicini) > 0 :
        nodoCorrente = codaVicini.pop(0) #Prendo un nodo dalla coda, mettendo l'indice garantisco FIFO e mi muovo in ampiezza
        for nodoVicino in neighbors(G, nodoCorrente): #Scorro la lista dei nodi vicini, alla prima iterazione quelli vicini ad s
            if not nodiVisitati[nodoVicino]: #Se non l'ho visitato lo visito e controllo
                nodiVisitati[nodoVicino] = True
                if nodoVicino == t: 
                    return True #Ho trovato il nodo
                codaVicini.append(nodoVicino) #Inserisco il nodo per poi elaborare i suoi di vicini
    return False #Non esiste un percorso da S a T
'''
STUDIO COMPLESSITÀ TEMPORALE
Dipende molto dalla funzione neighbors che a sua volta dipende dall'implementazione fisica del grafo.
Liste di adiacenza: scorriamo i nodi e gli archi quindi O(n+m) dove m sono gli archi
Matrice di adiacenza: O(n^2) poiché scorriamo n nodi con una complessità di neighbors O(n)
Nel caso migliore terminiamo con O(1) e ci fermiamo al primo if
STUDIO COMPLESSITÀ SPAZIALE
Oltre alle implementazioni fisiche del grafo abbiamo un vettore visitati lungo O(n)
'''
def raggiungibileDFS(G, S, T): #Deve essitere un cammino da s a t con visita in profondità, cambia soltanto il tipo di coda, qui usiamo LIFO per scendere più in basso possibile
    if ( S == T ): return True #Esco subito per caso base
    nodiVisitati = [False]*G.size() #Devo tenere conto dei nodi che ho già visitato per non andare in loop
    #Comincio il setup algoritmico di partenza
    nodiVisitati[S] = True #Perché devo partitre dela nodo S
    stackVicini = [S] #Comincio a scorrere i nodi vicino ad S
    while len(stackVicini) > 0 : #Finché ho nodi da esplorare
        nodoCorrente = stackVicini.pop() #Non metto indice per garantire LIFO, al primo giro prendo il nodo S inserito prima
        #Inizio a prendere in considerazione i vicini del nodo estratto dalla coda
        for nodiVicino in neighbors(G, nodoCorrente): #Scorro la lista che mi ritorna la funzione scritta precedentemente
            if not nodiVisitati[nodiVicino]: #Se il vicino del nodo estratto non è stato visitato mi sposto su di esso visitandolo, chiedendonmi se è T
                nodiVisitati[nodiVicino] = True #Prendo in considerazione il vicino
                if nodiVicino == T: return True #Ho trovato il nodo
                stackVicini.append(nodiVicino) #Inserisco il nodo che ho appena visitato per poi andare su di esso e controllare i suoi vicini, scendendo in profondità
    return False #Non sono riuscito a trovare un percorso da S a T
'''
COMPLESSITÀ TEMPORALE
Sostanzialmente questa funzione in base a come viene implementato concretamente il grafo cambia di molto la sua complessità, con le lista di adiacenza una DFS classica
ha complessità O(n+m) poiché scorriamo tutti gli n nodi e i loro archi nel caso peggiore, con matrice di adiacenza ogni nodo ha n elementi da controllare O(n^2).
Tenendo conto però della nostra funzione neighbors scritta in modo generico che ha complessità O(n) chiamata per n volte riduciamo il tutto a O(n^2) indipendentemente
dal tipo di implementazione del grafo.
COMPLESSITÀ SPAZIALE
La nostra funzione al suo interno usa un vettore con n celle per tenere conto dei nodi visitati con una complessità di O(n), utilizza anche una pila che non dipende
come nel caso della BFS da quanto il grafo sia largo ma potrebbe arrivare nel peggiore dei casi ad avere anche essa n elementi. Quindi usiamo uno spazio ausiliario
tralasciando lo spazio del grafo di al più O(n)
'''
def esisteCamminoCosto(G, S, T, costoLimite): #Deve esistere un cammino da S a T con costo totale <= costo
    #Proviamo ad implementare la funzione con una visita DFS e il backtracking
    if ( S == T ):
        return True
    
    nodiVisitati = [False] *G.size() #Devo tenere conto dei nodi che visito
    
    return dfsCosto( G, S, T, costoLimite, 0, nodiVisitati ) #Visita DFS con ricorsione e BackTracking

def dfsCosto( G, nodo, T, costoLimite, costoAttuale, nodiVisitati):
    #Sostanzialmente chiamo ricorsivamente questa funzione per esplorare un cammino, se non si può ritenere valido non lo tengo in considerazione e riparto da un nodo precedente
    #Non posso usare la semplice DFS poiché un nodo viene visitato una volta soltanto e quindi questo mi toglie la possibilità di visitarlo da un altro nodo di arrivo che ha costo minore
    #Siccome verrà chiamata ricorsivamente cominciamo a scrivere le condizioni di uscita dalla chiamata
    if ( costoAttuale > costoLimite ):
        return False #Il cammino eccede il costo limite, quindi va scartato
    if ( nodo == T ):
        return True #Ho trovato il cammino
    #Se il costo del cammino è minore uguale a quello limite ma non sono ancora arrivato a T devo andare più in profondità con la DFS chiamo quindi i suoi vicini
    nodiVisitati[nodo] = True #Marco il nodo come visitato e mi sposto sui suoi vicini
    for nodivicini, pesoVicini in neighbors(G, nodo): #Prendo la lista dei vicini con i relativi pesi
       if not nodiVisitati[nodivicini]: #Se il vicino non fa parte del cammino attuale mi sposto su di esso
            if dfsCosto ( G, nodivicini, T, costoLimite, costoAttuale+pesoVicini, nodiVisitati ):
                #Se il  percorso lungo questo nodo mi restituisce True è quello corretto
                return True
    nodiVisitati[nodo] = False #Sblocco il nodo poiché scorrendo tutti i percorsi dei suoi vicini nessuno mi ha dato true quindi non ci sono percorsi giusti da questo nodo con la strada precedente andando avanti
    #Qui c'è il backTracking, torno indietro e segno come non visitato questo nodo cosi ci posso arrivare da un altro percorso creato con i nodi precedenti
    return False
'''
COMPLESSITÀ TEMPORALE
Nel peggiore dei casi scorriamo con la visita DFS tutti i possibili cammini senza trovare quello giusto con una complessità di O(n!) però in ogni chiamata ricorsiva richiamiamo la nostra funzione
neighbors che abbiamo discusso in precedenza avendo complessità O(n) che porta tutto a O(n*n!) nel peggiore dei casi.
Ovviamente se miglioriamo la funzione neighbors con un implementazione a liste discussa precedentemente togliamo complessità.
COMPLESSITÀ SPAZIALE
Lo stack si riempie di tutte le chiamate ricorsive attive che possono essere un massimo di O(n) oltre al vettore ausiliario stanziato per i visitati O(n)x\x
'''
def esisteCamminoCostoBFS( G, S, T, costoLimite ): #Stessa funzione precedente implementata con visita BFS
    if ( S == T ): #Caso migliore
        return True
    #Comincio il setup per una visita BFS adattata a questa funzione
    #NON INSERISCO IL VETTORE DEI VISITATI POICHÈ DEVO POTER VISITARE LO STESSO NODO DA DIVERSI NODI DI ARRIVO IN PERCORSI DIFFERENTI
    coda = [] #Qui metterò tutti i nodi da visitare
    coda.append([S, 0, [S]]) #Nella coda avremo il nodo, il costo per arrivarci e il percorso da cui siamo arrivati
    while len(coda) > 0: #Inizio visita
        nodoAttuale, costoAttuale, percorsoAttuale = coda.pop(0) #Prendo i nodi in ordine 
        for nodoVicino, pesoVicino in neighbors(G, nodoAttuale): #Comincio a scorrere i vicini
            if nodoVicino not in percorsoAttuale: #Se il nodo è presente nel percorso non lo prendo
                nuovoCosto = costoAttuale + pesoVicino
                if nuovoCosto <= costoLimite: #Controllo quanto mi costa spostarmi sul vicino e se posso farlo senza eccedere il limite
                    if nodoVicino == T:
                        return True #Sono arrivato a destinazione
                    #Devo aggiungere il nodo al percorso
                    nuovoPercorso = percorsoAttuale + [nodoVicino]
                    #Aggiorno il cammino mettendolo in coda
                    coda.append([ nodoVicino, nuovoCosto, nuovoPercorso ]) #Questo è il nuovo percorso fino al nodo vicino
    return False #Non esiste il cammino cercato
'''
COMPLESSITÀ TEMPORALE
Supponendo di avere come al solito una coda ottimizzata per l'inserimento e l'estrazione rapida con costo O(1), la nostra funzione utilizza neighobors che ha costo O(n)
ed esplora in ampiezza più percorsi differenti, O(n!) senza parlare poi della lista dei percorsi O(n) e dell'if chiamato ogni volta per controllare se un nodo è nel percorso
O(n) porta la complessità in modo generale nel peggiore dei casi a O(n*n!)
COMPLESSITÀ SPAZIALE
Possiamo avere come spazio occupato i percorsi esplorati con un spazio interno di n che non hanno condotto a True la nostra funzione, anche qui O(n*n!)
'''
def esisteCamminoKBFS( G, S, T, limiteArchi ): #Deve esistere un cammino con al massimo k archi da S a T
    #Prima implementazione con visita BFS, scandisco più percorsi in maniera efficiente trovando naturalemente quello migliore
    if ( S == T ): return True #Caso migliore
    nodiVisitati = [False]*G.size() #Perché non devo visitare un nodo due volte
    nodiVisitati[S] = True #Comincio il percorso visitando il nodo di partenza
    coda = [] #Qui mettiamo tutti i nodi da esplorare
    coda.append([S, 0]) #Tengo per ogni percorso il numero di archi che lo compongono con un distanza dal primo nodo
    while len(coda) > 0:
        nodoAttuale, distanzaAttuale = coda.pop(0) #Comincio a scorrere il percorso cercando di muovermi in avanti
        #Controllo se posso aggiungere un arco al percorso attuale
        if  distanzaAttuale  < limiteArchi: #Ogni percorso ha un tot di archi
            for nodivicini in neighbors( G, nodoAttuale ): #Comincio a scorrere i nodi vicini per capire dove spostarmi
                if not nodiVisitati[nodivicini]: #Se non l'ho visitato mi sposto su di esso e controllo
                    #Mi sposto su di esso e lo segno come visitato
                    nodiVisitati[nodivicini] = True #Segnato come visitato
                    if (nodivicini == T):
                        return True #Sono arrivato a destinazione
                    #Metto nella coda il nodo su cui mi sono spostato per controllare poi i suoi vicini e aggiorno il percoso fino a questo punto
                    coda.append([nodivicini, distanzaAttuale+1]) #Appunto: Nella coda potresti tenere anche l'intero percorso ma è dispendioso in termini di spazio
    return False #Non sono riuscito a trovare il percorso
'''
STUDIO COMPLESSITÀ TEMPORALE
Supponendo di avere una coda con inserimento e estrazione pari ad O(1), la nostra funzione scorre i possibili cammini del grafo  con archi minori del limite k 
chiamando la funzione inizialmente scritta per i vicini con costo O(n). 
Portando il costo della visita BFS classica O(n+m) a O(n^2) poiche visitiamo gli n nodi almeno una volta chiamando la funzione neighbors con costo O(n)
STUDIO COMPLESSITÀ SPAZIALE
Oltre allo spazio occupato dal grafo abbiamo un vettore per tenere traccia dei nodi visitati che è al più O(n) e nella coda abbiamo i nodi percorsi che possono
essere al più n, quindi abbiamo un complessità totale nel peggiore dei casi di O(n)
'''
def esisteCamminokDFS( G, S, T, limiteArchi ):
    #Stessa funzione di prima ma con visita DFS, non trova naturlamente il miglior cammino ma si ferma al primo valido
    if ( S == T ): return True #Caso migliore
    #Cominciamo il setup per la visita, ovviamente deve essere ricorsiva e usare il backtracking poiché dobbiamo scandire tutti i cammini
    nodiVisitati = [False] * G.size() #Vettore dei visitati
    return KDFS( G, S, T, limiteArchi, nodiVisitati, 0 ) #Chiamata alla funzione ricorsiva per svolgere l'esercizo, gli passo anche la distanza oltre ai limite e i nodi visitati

def KDFS ( G, nodoAttuale, T, limiteArchi, nodiVisitati, distanza ):
    #siccome è una chiamata ricorsiva devo controllare se la distanza del percorso attuale è fuori limite
    if (distanza > limiteArchi ): return False #Il percorso non è valido
    if ( nodoAttuale == T ): return True #Ho trovato il percorso
    nodiVisitati[nodoAttuale] = True #Segno il nodo come visitato e comincio a scorrere i vicini
    for nodivicini in neighbors(G, nodoAttuale): #Comincio a scorrere i nodi vicini a quello attuale
        if not nodiVisitati[nodivicini]: #Visito il nodo
            if KDFS ( G, nodivicini, T, limiteArchi, nodiVisitati, distanza+1 ):
                return True #Mi sposto su quel nodo e do true se la chiamata ricorsiva avviata mi da True quando torna da me
    #Se non ho trovato ricorsivamente il percorso e la ricorsione non mi ha dato True torno indietro e faccio backtracking
    nodiVisitati[nodoAttuale] = False #Poichè il nodo attuale potrebbe essere utilizzato per un altro percorso
    return False #Non abbiamo trovato il percorso
'''
STUDIO COMPLESSITÀ TEMPORALE
La nostra funzione scorre in modo ricorsivo i nodi del grafo fino a trovare il percorso valido che soddisfa le condizioni chiamando nel peggiore dei casi la nostra funzione
neighobors con costo O(n) per tutti i nodi esplorando tutti i cammini possibili portando la complessità a O(n^n) poiché con il backtracking possiamo visitare più volte un nodo
STUDIO COMPLESSITÀ SPAZIALE
Oltre allo spazio occupato dal nostro grafo abbiamo lo stack pieno di chiamate ricorsive che possono essere nel peggiore dei casi pari ad n portando la complessità a O(n)
'''
def kruskal(G):
    #Kruskal mi costruire il minimo albero ricoprente del grafo, sostanzialemente collego tutti i nodi con archi di costo minimo, ragioniamo sul costo degli archi
    #Comincio a prendere tutti gli archi del nostro grafo
    archi = [] #lista di tutti gli archi del grafo
    nodiVisitati = [False]*G.size() #Mi serve per non duplicare gli archi del grafo dato che non è orientato
    nodiGrafo = G.nodes() #Prendo la lista dei nodi per poter ricostruire gli archi
    for nodo in nodiGrafo: #Scorro la lista dei nodi
        for nodoVicino in neighbors(G, nodo): #Prendo i vicini di ogni nodo
            if not nodiVisitati[nodoVicino]: #Controllo per non inserire due volte l'arco, dato che non è orientato
                pesoArco = G.getWeight(nodo, nodoVicino) #Mi faccio restituire il peso
                archi.append([nodo, nodoVicino, pesoArco]) #Inserisco l'arco con il peso nella lista
        nodiVisitati[nodo] = True #Quindi il nodo attuale non verra preso in considerazione una volta che mi sposto sui prossimi nodi
    archi.sort(key= lambda arco:arco[2]) #Ordino la lista per il campo pesoArco in modo crescente
    #Da questo momento in poi dobbiamo cominciare a creare il nosto albero ricoprente scorrendo gli archi ordinati che abbiamo preso in considerazione prima
    mst = Graph(G.size()) #Questo grafo rappresenta il nostro MST
    albero = [] #Lista degli archi che ho scelto
    #Cominciamo a scorrere gli archi
    for arco in archi:
        nodo1 = arco[0] #Mi prendo il primo nodo
        nodo2 = arco[1] #Mi prendo il secondo nodo
        peso = arco[2] #Prendo anche il peso dell'arco
        if not raggiungibileBFS(mst, nodo1, nodo2): #Recupero il codice scritto in precedenza
            albero.append(arco) #Aggiungo l'arco alla lista
            mst.insertEdge(nodo1, nodo2, peso) #Costruisco l'albero
        #Appena ho n-1 archi ho termianto kruskal poiché significa che ho collegato tutt i nodi
        if len(albero) == G.size()-1:
            break
    return albero #Lista degli archi scelti
'''
STUDIO COMPLESSITÀ TEMPORALE
Siccome non è l'implementazione classica di kruskal con la union find ma è una nostra implementazione la complessità è un po' differente da quella classica.
Cominciamo con lo scorrere n volte la nostra funzione neighbors per costruire la lista degli archi con una complessità di O(n^2)
Dopodiché abbiamo un ordinamento semplice di una lista che costa al più O(mlog m) dove m sono gli archi, i componenti della lista
Per ogni arco scorriamo nuovamente con una visita BFS il grafo che stiamo costruendo in cui al suo interno richiama nuovamente neighbors portando la complessità a
O(mn^2) dove m sono gli archi e n sono i nodi. La nostra implementazione di kruskal ha quindi complessità O(m*n^2)
STUDIO COMPLESSITÀ SPAZIALE
Abbiamo un vettore per gli archi O(m) e un altro vettore per i nodi O(n) quindi O(m+n) in generale
'''

#Da questo punto in poi riscrivo Kruskal in maniera ottimizzata, con la union-find, l'implementazione standard

def find(padre, nodo): #Questa funzione restituisce il padre di ogni nodo passato interrogando un vettore che si aggiorna ciclicamente
    #Ciclicamente interrogo il vettore fino ad arrivare  a me stesso
    #Supponiamo di avere [0,0,1,3] e vogliamo trovare il padre del nodo 2, faremo find(padre, 2) che chiamerà find(padre, 1), poi find(padre, 0) e solo questa darà 0
    #Sono sceso ricorsivametne nell'array trovando il cammino 2<-1<-0 quindi il padre di 2 è 0
    if padre[nodo] == nodo: #Se la chiamata accede ad una cella con il valore del nodo stesso quello è il padre, non posso andare più indietro
        return nodo
    find(padre, padre[nodo]) #Chiamo il padre del nodo presente nella cella passata, in caso ci sia un nodo di mezzo
    
def union(padre, nodo1, nodo2): #Unisco i nodi in un solo insieme
    #Trovo i padri dei nodi
    radice1 = find(padre, nodo1)
    radice2 = find(padre, nodo2)
    #Se non hanno lo stesso padre vuol dire che non crea ciclo unirli
    if radice1 != radice2:
        padre[radice2] = radice1 #Il nodo 1 è diventato padre del nodo 2, ho aggiunto il nodo 2 all'insieme del nodo 1
    return padre #Ritorno il vettore aggiornato

def kruskalStandard(G): #Implementazione con la union-find, kruskal in modo strandard
    #Kruskal mi costruire il minimo albero ricoprente del grafo, sostanzialemente collego tutti i nodi con archi di costo minimo
    #Comincio a prendere tutti gli archi del nostro grafo
    archi = [] #lista di tutti gli archi del grafo
    nodiVisitati = [False]*G.size() #Mi serve per non duplicare gli archi del grafo dato che non è orientato
    nodiGrafo = G.nodes() #Prendo la lista dei nodi per poter ricostruire gli archi
    for nodo in nodiGrafo: #Scorro la lista dei nodi
        for nodoVicino in neighbors(G, nodo): #Prendo i vicini di ogni nodo
            if not nodiVisitati[nodoVicino]: #Controllo per non inserire due volte l'arco, dato che non è orientato
                pesoArco = G.getWeight(nodo, nodoVicino) #Mi faccio restituire il peso
                archi.append([nodo, nodoVicino, pesoArco]) #Inserisco l'arco con il peso nella lista
        nodiVisitati[nodo] = True #Quindi il nodo attuale non verra preso in considerazione una volta che mi sposto sui prossimi nodi
    archi.sort(key= lambda arco:arco[2]) #Ordino la lista per il campo pesoArco in modo crescente
    #Da questo punto in poi cambia, introduco il vettore dei padri
    padre = list(range(G.size())) #Vettore con inizialmente i padri dei nodi impostati su loro stessi
    mst = Graph(G.size()) #Creo un grafo per poi usarlo come MST
    for arco in archi: #Comincio a scorrere gli archi
        nodo1, nodo2, peso = arco #Prendo i valori di ogni arco
        #controllo con la find se appartengono ad insiemi diversi
        if find(padre, nodo1) != find(padre, nodo2): #Non hanno lo stesso padre => non sto creando ciclo
            mst.insertEdge(nodo1, nodo2, peso) #Aggiungo l'arco al MST
            union(padre, nodo1, nodo2) #Unisco il nodo 2 all'insieme del nodo 1
    return mst #Ritorno il minimo albero ricoprente
'''
STUDIO COMPLESSITÀ TEMPORALE
Sostanzialmente fino alla creazione dell'insieme degli archi e al loro ordinamento la funzione resta la stessa, chiamiamo la nostra funzione neighbors n volte portando
la complessità o(n^2) per la creazione della lista degli archi che poi verrà ordinata con un costo di O(mlog m) dove m sono gli archi, cioè gli elementi della lista.
Dopodiché cambia tutto poichè la union find migliora di molto l'aspetto, nel ciclo ora abbiamo uno scorrimento di un vettore padre anziché una visita BFS del grafo,
questo vettore nel peggiore dei casi mi può portare ad uno scorrimento pari ad n, tutti i nodi sono in un insieme, fatto per m volte.
La complessità sarà quindi: O(n^2) + O(mlog m) + O(m*n) su grandi numeri prevarrà O(m*n).
N.B.: 
Il prof ottimizza ancora di più la find spostando l'insieme più piccolo in quello più grande e usando un heapsort per ordinare la lista ma il tempo passa e l'esame è dopodomani, mi fermo qui
STUDIO COMPLESSITÀ SPAZIALE
Lo spazio utilizzato è O(n+m) perché abbiamo un mst creato con n nodi e m archi, il vettore padre è lungo n ed infine la lista archi è lunga m
'''
def prim(G, nodoSorgente):
    #Prende un nodo di partenza e comincia a creare un albero inserendo gli archi uscenti dal nodo, ogni volta prende l'arco più economico uscente da un nodo dell'albero
    nodiVisitati = [False]*G.size() #Tengo conto dei nodi che ho visitato per non inserirli due volte
    nodiVisitati[nodoSorgente] = True #Il nodo di partenza e già innserito nel MST
    mst = Graph(G.size()) #Creazione del MST
    for i in range(G.size()-1): #Comincio a scorrere gli archi, ogni iterazione ne aggiungo uno al nostro MST
        pesoMinimo = math.inf() #Valore fittizio da controllare
        for nodoGrafo in G.nodes(): #Comincio a scorrere i nodi del grafo
            if nodiVisitati[nodoGrafo]: #Pre prendere gli archi uscenti dai nodi che ho già nel MST, alla prima iterazione sarà il nodoSorgente passato
                #Qui comincio a scorrere gli archi uscenti del nodo nel MST
                for nodoVicino in neighbors(G, nodoGrafo):
                    if not nodiVisitati[nodoVicino]: #Se non è stato aggiunto al MST/visitato controllo il peso dell'arco
                        pesoArco = G.getWeigth(nodoGrafo, nodoVicino) #Prendo il peso dell'arco
                        if pesoArco < pesoMinimo: #Ho trovato il nuovo arco con peso minimo
                            pesoMinimo = pesoArco #Aggiorno il valore
                            nodoScelto = nodoVicino #Salvo il nodo di arrivo
                            nodoPartenza = nodoGrafo #Salvo il nodo di partenza
        nodiVisitati[nodoScelto] = True #Faccio entrare il nodo scelto nel MST/Visito
        mst.insertEdge(nodoPartenza, nodoScelto, pesoMinimo) #Aggiungo i nodi e l'arco al MST
    return mst #Ritorno l'albero
'''
STUDIO COMPLESSITÀ TEMPORALE
La nostra funzione scorre n-1 volte i vicini dei nostri n nodi chiamando la funzione neighbors per n volte portando la complessità a O(n^3) poiché chiamo n volte neighbors con costo n per n-1 volte.
Il tutto supponendo che il recupero del pesso dell'arco costi O(1) altrimenti va tenuto in considerazione anche quello
STUDIO COMPLESSITÀ SPAZIALE
Lo spazio ausiliario usato è O(n) poiché abbiamo il vettore dei visitati e il MST con n nodi al suo interno
'''
def dijkstraSemplice(G, nodoSorgente):
    #dijkstra mi trova il cammino di costo minimo attraversando più nodi in mezzo, dalla sorgente verso un nodo
    distanza = [math.inf()]*G.size() #Imposto le distanze ad un valore fittizio per aggiornarle poi
    nodiVisitati = [False]*G.size() #Tengo conto dei nodi con distanza ottima da non modificare
    distanza[nodoSorgente] = 0 #Poichè è il nodo di partenza
    for i in range (G.size()): #Devo controllare le distanze di un nodo verso gli altri per ogni nodo
        distanzaMinima = math.inf() #Valore fittizio da aggiornare
        nodoAttuale = None #Cerco un nodo da visitare, quello con distanza minima nel vettore delle distanze
        for nodoGrafo in G.nodes(): #Comincio a scorrere i nodi non visitati che hanno una distanza aggiornabile
            if not nodiVisitati[nodoGrafo] and distanza[nodoGrafo]<distanzaMinima: #Alla prima iterazione passa il nodo sorgente da qui
                #Salvo le info del nodo per aggiornare le distanze da lui verso gli altri
                distanzaMinima = distanza[nodoGrafo]
                nodoAttuale = nodoGrafo
        if nodoAttuale is None:
            break #Non ho trovato altri nodi con distanze aggiornabili
        nodiVisitati[nodoAttuale] = True #Mi sposto sul nodo per scorrere i suoi vicini, quindi lo segno come visitato
        for nodoVicino in neighbors(G, nodoAttuale): #Scorro la lista dei nodi vicini a quello selezionato
            if not nodiVisitati[nodoVicino]: #Se non ho ancora visitato i nodi vicini analizzo l'arco
                pesoArco = G.getWeigth(nodoAttuale, nodoVicino) #Prendo il peso dell'arco
                nuovaDistanza = distanza[nodoAttuale]+pesoArco #Simulo quanto mi costa spostarmi con questo arco al vicino
                if nuovaDistanza < distanza[nodoVicino]:
                    distanza[nodoVicino] = nuovaDistanza #Aggiorno se la distanza e favorevole
                    #Passando per nodoAttule la distanza è minore di quella che conoscevo
    return distanza #Ritorno il vettore delle distanze minime dal nodo sorgente
'''
STUDIO COMPLESSITÀ TEMPORALE
La nostra funzione per tutti gli n nodi richiama due cicli importanti, il primo scorre i nodi quindi O(n) il secondo i vicini con la complessità
della funzione neighbors O(n) il tutto per n volte come detto all'inzio, portando la complessità a O(n^2) supponendo di avere per il ricavo del peso O(1)
STUDIO COMPLESSITÀ SPAZIALE
Oltre al grafo abbiamo i vettori che ci servono come aiuto O(n) poichè non eccedono lunghezza n
'''
def dijkstraPQ(G, S, T):
    #Proviamo ad implementare la stessa funzione di dijkstra con un nodo sorgente e uno terminale e stampare anche il percorso attraversato con una coda a priorità
    distanzaNodi = [math.inf()]*G.size() #Vettore con le distanze dei nodi, inizialmente valore fittizi da aggiornare
    distanzaNodi[S] = 0 #La distanza dal nodo di partenza è zero
    nodiVisitati = [False]*G.size() #Vettore per segnare un nodo come visitato ed elaborato il cammino migliore per arrivarci
    predecessori = [None]*G.size() #Lista in cui inserisco tutti i nodi che ho attraversato per trovare T, inizialmente celle vuote da rimepire
    coda = [(distanzaNodi[S], S)] #Coda in cui inserisco i nodi da visitare e controllare, [Distanza, nodo]
    #Siccome la implemento come una coda a priorità nell'estrazione ottengo sempre il nodo con distanza più piccola
    while len(coda) > 0:
        distanzaAttuale, nodoAttuale = heapq.heappop(coda) #Estrazione dalla coda, abbiamo già il nodo con distanza minima quindi saltiamo il for precedente per cercare la distanza minima
        if nodiVisitati[nodoAttuale]:
            continue #Potrebbe capitare di trovare un nodo già visitato quindi passo avanti
        #Se il nodo non è stato visitato lo segno
        nodiVisitati[nodoAttuale] = True
        if nodoAttuale == T:
            break #Significa che sono già arrivato a T con la distanza minima possibile
        #Scandisco i nodi suoi vicini se non è T per controllare se posso aggiornare le distanze
        for nodoVicino in neighbors(G, nodoAttuale):
            if not nodiVisitati[nodoVicino]:
                #Prendo in consiedarzione l'arco come nel codice precedente
                pesoArco = G.getWeigth(nodoAttuale, nodoVicino)
                nuovaDistanza = distanzaAttuale + pesoArco #La distanza attuale fino all'arco in cui mi trovo, l'estratto dalla coda
                if nuovaDistanza < distanzaNodi[nodoVicino]: #Se la nuova distanza con il nuovo arco è favorevole la prendo in considerazione
                    distanzaNodi[nodoVicino] = nuovaDistanza #Aggiornamento distanza
                    predecessori[nodoVicino] = nodoAttuale #Aggancio il predecessore migliore
                    heapq.heappush(coda, (distanzaNodi[nodoVicino], nodoVicino)) #Per poi estralo e controllare se posso nuovamente aggiornare la distanza
    #Finita la coda o trovato il nodo T devo restituire il vettore predecessori con i nodi attraversati
    #Prima però controllo se ci sono arrivato altrimenti restituisco un valore base
    if distanzaNodi[T] == math.inf():
        return -1 #T è irraggiungibile
    percorso = [] #Lista finale del percorso da t a s
    nodo = T #Nodo finale
    while nodo is not None: #Scorro la lista fino a quando non prendo il predecessore di S che è None
        percorso.append(nodo) #Aggiungo il nodo al percorso
        nodo = predecessori[nodo] #Prendo il prossimo predecessore
    return percorso #Percorso 
'''
STUDIO COMPLESSITÀ TEMPORALE
La nuova parte con L'heap nel caso peggiore ha costo O(m*log n) poiché un nodo può essere inserito m volte con costo O(log n). Nella parte dei vicini per come viene
elaborata la neighbors implementata a monte di questo file abbiamo costo O(n) che nel peggiore dei casi viene richiamata per ogni nodo n portando il tutto a O(n^2).
La creazione della lista percorso ha costo O(n) nel peggiore dei casi. In generale quindi nel peggiore dei casi avremo O(n^2+m*log n)
STUDIO COMPLESSITÀ SPAZIALE
Nel peggiore dei casi l'heap viene riempito per O(m) elementi mentre tutti gli altri costano O(n).
Qui la complessità sarà quindi O(m+n)
'''
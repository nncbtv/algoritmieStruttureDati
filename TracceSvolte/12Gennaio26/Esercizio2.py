#Importo la classe con tutte le primitive e per rappresentare il grafo
from Codici.GraphL import Graph
import math

G = Graph(5) #Grafico con 5 nodi per esempio

def sceltaProssimo ( distanzaNodi, nodoVisitato ):
    x = math.inf #Valore fittizio per poi aggiornalo
    y = -1 #Valore fittizio per poi aggiornarlo con il nodo
    for i in range ( len(distanzaNodi) ): #Comincio a scorrere i nodi
        if ( not nodoVisitato[i] ) and (distanzaNodi[i]<x): #Se non è stato visitato e la distanza è minore di x, primo passo sicuramente
            y = i #Prendo il nodo
            x = distanzaNodi[i] #Assegno a x la distanza per poi controllarla al prossimo passo
    return y

def camminoMinimo(listaNodi, S, T): #Mi passa la lista dei nodi precedenti di Dijkstra e ritorno il cammino
    if listaNodi[T] == -1 and S!=T:
        return [] #Mi fermo subito se T non è raggiungibile e Dijkstra mi ha passato una lista non valida
    cammino = [] #Lista di ritorno 
    nodo = T #Nodo a cui sono arrivato con Dijkstra
    while nodo != S: #Comincio a scorrere all'indietro finché non arrivo all'inizio
        cammino.append(nodo) #Aggiungo il nodo
        nodo = listaNodi[nodo] #Prendo il nodo da cui sono arrivato prima e ricomincio il while
    cammino.append(S) #Aggiungo alla fine S
    cammino.reverse() #Inverto la lista per averla da inizio a fine
    return cammino

def camminiVincolati(G, S, T, nodiProibiti):
    #Presumo che S e T non siano mai contenuti nella lista proibita
    numeroNodi = G.size() #Numero di nodi presenti nel grafo
    distanzaNodi = [ math.inf for i in range(numeroNodi) ] #Setto ad infinito come valore fittizio, per poi aggiornarla ad ogni iterazione
    nodoPrecedente = [ -1 for i in range(numeroNodi) ] #Tengo conto da quale nodo sono arrivato
    nodoVisitato = [ False for i in range(numeroNodi) ] #Se un nodo è già stato visitato non lo rivisito
    distanzaNodi[S] = 0 #Il nodo di partenza dista da se stesso zero
    #Comincio l'esplorazione dei nodi
    nodiProibiti = set(nodiProibiti) #Trasformo la lista passata in un set per ottimizzare la ricerca ed ottenere ogni volta che chiamo l'if un costo O(1)
    for i in range (numeroNodi):
        nodoCorrente = sceltaProssimo (distanzaNodi, nodoVisitato) #Questa funzione sceglierà l'arco con costo minimo verso cui andare
        if nodoCorrente == -1 or nodoCorrente == T: #Se non trovo prossimi nodi la funzione mi restituisce -1 quindi gestisco il caso fermandomi oppure ho trovato T
            break
        if nodoCorrente not in nodiProibiti: #Se è un nodo valido continuo ad andare avanti
            nodoVisitato[nodoCorrente] = True
            #Comincio a scorrere i vicini di questo nodo
            viciniNodo = G.neighbors(nodoCorrente) #Lista dei vicini al nodo selezionato
            for nodo, peso in viciniNodo: #Scorrimento nodi vicini al selezionato per prendere quello con peso minore
                if nodo not in nodiProibiti: #Controllo se tra i vicini ci sono nodi proibiti
                    if not nodoVisitato[nodo]: #Prendo il vicino del nodo selezionato e solo se non l'ho già visitato prima continuo
                        pesoPercorso = distanzaNodi[nodoCorrente]+peso #Aggiorno la distanza con quella dell'arco in cui mi sposto
                        if ( pesoPercorso < distanzaNodi[nodo] ): #Controllo la distanza dal nodo sorgente fino al nodo in cui mi sono spostato
                            distanzaNodi[nodo] = pesoPercorso #La aggiorno se neccessario
                            nodoPrecedente[nodo] = nodoCorrente #Accodo il nodo da cui sono arrivato
    return distanzaNodi, camminoMinimo(nodoPrecedente, S, T) #Ritorno i nodi su cui sono passato

'''

Siccome per ogni chiamata a sceltaProssimo scorro tutti i nodi e lo faccio n volte ottengo una complessità di O(n^2)
Poi con Dijkstra esamino gli archi di un nodo ottenendo O(m) dove m sono il numero di archi ma siccome m<=n rimane o(n^2) nel caso generale
Per ottimizzare meglio anziché usare una lista per nodi proibiti che aumenta la complessità dato che devo cercare dentro di essa ogni volta il nodo preso in considerazione
implemento questo punto con un set portando così la ricerca ad O(1) altrimenti sarebbe stato O(|P|) e quindi un grave dispendio inutile

'''
def minPath(grafo, S, K): #Programmazione dinamica perché tengo conto anche dei valori precedenti restituiti prima di cambiare e andare avanti
    numeroNodi = grafo.size() #Numero di nodi presenti nel grafo
    distanzaNodi = [ math.inf for i in range(numeroNodi) ] #Setto ad infinito come valore fittizio, per poi aggiornarla ad ogni iterazione
    distanzaNodi[S] = 0 #Il nodo di partenza dista da se stesso zero
    #Comincio lo scorrimento degli archi e la programmazione dinamica
    for k in range(K): #Dovrò avere al massimo K archi, quindi non più di k iterazioni, per ogni iterazione scelgo un arco
        nuovaDistanza = distanzaNodi[:] #Mi copio la distanza dei nodi ad ogni iterazione per poi cercarne una migliore e modificarla solo se la trovo
        #Comincio a scorre i nodi del grafo
        for nodoCorrente in range(numeroNodi):
            if distanzaNodi[nodoCorrente] != math.inf: #entro in un nodo che posso visitare, ci sono arrivato da uno precedente oppure è il nodo S alla prima iterazione
                for prossimoNodo, peso in G.neighbors(nodoCorrente): #Comincio a scorrere i suoi vicini per capire se posso aggiornare le distanze
                    nuovaDistanza[prossimoNodo] = min (nuovaDistanza[prossimoNodo], distanzaNodi[nodoCorrente]+peso) #Scelgo il minimo tra la vecchia distanza e la nuova se dal nodocorrente mi sposto al prossimo
        distanzaNodi = nuovaDistanza #Aggiorno la lista della distanza dei nodi, solo dopo aver controllato se esistono archi migliori
    return distanzaNodi

'''

La complessità di questa funzione deriva dal fatto che viene eseguita k volte e ad ognuna di essa dobbiamo scorrere i nodi del grafo più la lista dei suoi vicini per aggiornare le distanze,
quindi abbaimo O(K(n+m)) nel caso peggiore m=n allora diventa n^2 dove k sono il numero massimo di archi passati per i cammini, n il numero di nodi e m sono gli archi

'''
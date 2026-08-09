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

def nodiAttraversati(listaNodi): #Mi passa la lista dei nodi precedenti di Dijkstra e ritorno solo quelli presi in considerazione
    E = []
    for i in range ( len(listaNodi) ):
        if listaNodi[i] != -1:
            E.append([listaNodi[i], i])
    return E

def camminiVincolati(G, S, T, nodiProibiti):
    #Presumo che S e T non siano mai contenuti nella lista proibita
    numeroNodi = G.size() #Numero di nodi presenti nel grafo
    distanzaNodi = [ math.inf for i in range(numeroNodi) ] #Setto ad infinito come valore fittizio, per poi aggiornarla ad ogni iterazione
    nodoPrecedente = [ -1 for i in range(numeroNodi) ] #Tengo conto da quale nodo sono arrivato
    nodoVisitato = [ False for i in range(numeroNodi) ] #Se un nodo è già stato visitato non lo rivisito
    distanzaNodi[S] = 0 #Il nodo di partenza dista da se stesso zero
    #Comincio l'esplorazione dei nodi
    for i in range (numeroNodi):
        nodoCorrente = sceltaProssimo (distanzaNodi, nodoVisitato) #Questa funzione sceglierà l'arco con costo minimo verso cui andare
        if nodoCorrente == -1: #Se non trovo prossimi nodi la funzione mi restituisce -1 quindi gestisco il caso fermandomi
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
    return distanzaNodi, nodiAttraversati(nodoPrecedente) #Ritorno i nodi su cui sono passato
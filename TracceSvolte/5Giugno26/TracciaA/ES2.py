#Comincio con importare le primitive per il grafico
from Codici.GraphL import Graph
import math
G = Graph(5) #creo il grafico

#Il grafo è non orientato ma pesato, il peso non va oltre una certa soglia c

def neighbors(G, nodo): #Deve resistuire tutti i vicini al nodo passato con il loro peso, da [nodo, peso]
    ris = [] #Lista dei vicini con pesi
    nodi = G.nodes() #Restituisce la lista dei nodi presenti nel grafo
    #Comincio a scorrere i nodi e cerco se esiste un arco tra i due
    for nodoCorrente in nodi:
        if (G.isEdge(nodo, nodoCorrente)): #Controllo se ho un arco tra i due nodi
            peso = G.getWeight(nodo, nodoCorrente) #Prendo il peso del nodo
            ris.append([nodoCorrente, peso]) #Aggiungo alal lista che devo restituire
    return ris #Ritorno la lista dei vicini con i relativi pesi

'''
STUDIO COMPLESSITÀ TEMPORALE
Nel caso peggiore il nodo passato si trova al centro del grafo e ha tutti gli altri nodi vicino ad esso quindi O(n) dove n sono i nodi del grafo.
STUDIO COMPLESSITÀ SPAZIALE
La lista dei nodi occupa una complessità O(n) se nel caso peggiore tutti sono vicini al nostro nodo abbiamo O(n) poiché dobbiamo ricreare una lista lunga n partendo da un lista lunga n
'''

def filterGraph(G, C): #Deve restituire un nuovo grafo con solo gli archi <= C ma con gli stessi nodi
    grafoFiltrato = Graph(G.size()) #Creo un nuovo grafo con lo stesso numero di nodi del passatoo
    for x in G.nodes():
        for y in G.nodes():
            if y>x: #Prendo il nodo x e x+1
                if G.isEdge(x,y): #Controllo se esiste l'arco
                    peso = G.getWeigth(x,y) #Prendo il peso dell'arco
                    if peso <= C: #Controllo se può essere aggiunto al grafo filtrato
                        grafoFiltrato.insertEdge(x, y, peso)
    return grafoFiltrato #Ritorno al grafo filtrato

'''
STUDIO COMPLESSITÀ TEMPORALE
Controllo un nodo con tutti gli altri, quindi scorro n volte la lista dei nodi O(n^2), in base a come viene implementato il grafo la complessità aumenta per lo scorrimento delle liste di adiacenza
nel caso peggiore dobbiamo scorrere altre n volte i vicini portando tutto a O(n^3)
STUDIO COMPLESSITÀ SPAZIALE
Creaiamo un grafo con n nodi che al massimo avrà n-1 archi tra di loro quindi nel peggiore dei casi è O(n^2) per entrambe le implementazioni
'''

def sceltaNodo (distanzaNodi, nodiVisitati):
    #Siccome il grafo è connesso scelgo il prossimo nodo scorrendo tra quelli non visitati e prendendo quello con distanza minima
    x = math.inf #Valore della distanza minimo
    y = -1 #Indice del nodo da prendere
    for i in range( len(distanzaNodi) ): #Scorro i nodi
        if (not nodiVisitati[i]) and (distanzaNodi[i]<x): #Controllo se non è stato visitato e se la distanza è minore del minimo
            y = i #Salvo l'indice del nodo
            x = distanzaNodi[i] #Salvo la nuova distanza minima
    #A fine scorrimento x sarà la distanza minima e y il nodo
    return y

def budgetedConnectionPrim(G, S, C): #Devo prendere un grafo filtrato con C e poi restituire l'insieme dei nodi e archi raggiungibili partendeo dal nodo S
    #Prim non mi dice quanto mi costa arrivare ad un nodo ma mi dice quale è l'arco più economico per collegarli tra di loro, creando un MSP del grafo
    grafoFiltrato = filterGraph(G,C) #Creo il nuovo grafo filtrato da cui partire per trovare i cammini raggiungibili senza superare C
    nodiVisitati = [ False for i in range (grafoFiltrato.size())] #Qui metto tutti i nodi raggiunti da S nel grafo filtrato, inizialmente false per poterli scorrere
    costo = [ math.inf for i in range ( grafoFiltrato.size()) ] #Questo è il costo degli archi presi in considerazione
    costo[S] = 0 #Sempre perché se stesso costa zero se ci vado
    nodoPrecedente = [ -1 for i in range ( grafoFiltrato.size()) ] #Per ricordarmi da quale nodo arrivo
    archi = [] #Archi per la soluzione che costituiscono il MSP
    for i in range ( grafoFiltrato.size() ):
        nodoCorrente = sceltaNodo(costo, nodiVisitati) #Scelta del nodo
        if nodoCorrente == -1:
            break #Non ho trovato il prossimo nodo su cui spostarmi
        nodiVisitati[nodoCorrente] = True #Il nodo passa nell'albero
        #Se il nodo preso in considerazione non è S aggiungo l'arco alla soluzione
        if nodoCorrente != S:
            peso = costo[nodoCorrente]
            archi.append([nodoPrecedente[nodoCorrente], nodoCorrente, peso]) #Aggiunta alla lista degli archi scelti
        #Aggiorno i costi dei vicini
        for nodoVicino, pesoVicino in neighbors(grafoFiltrato, nodoCorrente): #Comincio a scorrere i vicini del mio nodo
            if not nodiVisitati[nodoVicino]: #Se non sono stati visitati
                if pesoVicino < costo[nodoVicino]: #Se il peso fin ora è minore di quello memorizzato lo aggiorno
                    costo[nodoVicino] = pesoVicino
                    nodoPrecedente[nodoVicino] = nodoCorrente #Mi segno da quale nodo sono arrivato al vicino
    nodiRaggiunti = [] #Perché ho solo l'elenco dei nodi che ho visitato quindi ne devo creare uno in cui sono presenti questi nodi dall'appello dei nodi visitati
    for nodo in range (grafoFiltrato.size()):
        if nodiVisitati[nodo]:
            nodiRaggiunti.append(nodo)
    return (nodiRaggiunti, archi)        
        
'''
STUDIO COMPLESSITÀ TEMPORALE
Cominciamo con il dire che scelta nodo scorre tutti gli n nodi, O(n) chiamata per n volte, O(n^2), dobbiamo anche scorrere gli archi di ogni nodo quindi O(m) ma essendo m<n resta O(n^2)
COMPLESSITÀ SPAZIALE
Otteniamo una complesità di O(n), giusto lo spazio di riempire le liste ausiliarie che ci servono per prim oltre allo spazio già occupato dal grafo ecc.
'''

#Si può risolvere l'ultimo punto anche con kruskal ma è molto più complesso, la complessità non vale la candela
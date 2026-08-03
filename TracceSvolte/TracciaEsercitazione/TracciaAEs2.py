#TRACCIA A ESERCITAZIONE

#ESERICIZIO 2

#Per questo esercizio scelgo di implementare il grafo con una matrice di adiacenza importando dalle classi del prof
from Codici.GraphM import Graph

G = Graph(4) #Creo il grafico richiesto dalla traccia, 5 valore fittizio per provare

#Funzione richiesta da implementare nella traccia
def independent(G, S):
    
    #Controllo prima condizione su S
    
    if S == []: return False #Se il sottoinsieme passato è vuoto non posso continuare
    for x in S: #Nella lista S non ci devono essere nodi che non abbiamo nel grafo
        if x not in G.nodes():
            return False
    #Se contiene nodi del grafo e la lunghezza è identica alla lista nodi, contiene tutti i nodi del grafo
    if len(S) == len(G.nodes()): return False 
    
    #Controllo seconda condizione su S
    #Siccome il grafo non è orienntato mi basta controllare ogni nodi con i prossimi
    for x in range (len(S)): #Comincio con prendere il primo nodo e scorrere normalmente
        for y in range (x+1, len(S)): #Comincio dal prossimo del precedente
            if S[x] != S[y]: #Controllo se sono nodi diversi
                if G.isEdge(S[x], S[y] ): #Se hanno un arco S non è valido
                    return False

    #Punto 3
    """
    Risulta ambiguo, non posso creare una BST da un grafo non orientato, non ho informazioni per costruirlo.
    Probabilmente il prof avrà inserito un altro dettaglio tralasciato dalla traccia e detto a voce a lezione
    """
    """
    STUDIO DELLA COMPLESSITÀ ALGORITMICA
    Fisso prima di tutto n il numero di nodi del grafo e k il numero di nodi della lista S.
    Nel caso peggiore dato che S è un sottoinsieme dei nodi possiamo avere k<=n.
    Riga 15: controllare una lista vuota è pari a O(1)
    Riga 16-17: Il ciclo viene eseguito K e l'if invece deve creare ogni volta la lista di nodi del grafo quindi O(n) => O(k*n) se però nel caso peggiore k=n diventa O(n^2)
    Riga 20: Controllo della lunghezza costa un tempo O(1) ma siccome devo creare una lista di nodi con g.nodes diventa O(1*n) => O(n)
    Riga 24-28:
        Il primo ciclo viene ripetuto per k volte, il secondo ciclo viene ripetuto in modo decrescente di k fino ad arrivare a 0 ((k-1)+(k-2).....+0) 
        riconducibile al coefficinete binomiale (k(k-1))/2
        Quindi O(k^2) in modo grossolano
    Complessità generica: O(k*n)+O(n)+O(k^2)
    Il caso peggiore si verifica quando k=n perché la complessità si riduce a O(n^2)
    """
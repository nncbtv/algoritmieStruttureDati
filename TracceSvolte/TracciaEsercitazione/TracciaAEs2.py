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
    
    #Rimozione nodi
    
#Lalbero è definito come tripla [valore, sinistra, destra]
def BST():
    return []

def empty(A):
    return A == []

def key(A):
    return A[0] if not empty(A) else None

def left(A):
    return A[1] if not empty(A) else []

def right(A):
    return A[2] if not empty(A) else []

# Aggiunta nodo foglia - crea un nuovo nodo con valore x
def addNode(x):
    return [x, [], []]

#Funzione ricerca ricorsiva
def search(A, x):
    if empty(A):
        return False
    if A[0] == x:
        return True
    elif x < A[0]:
        return search(A[1], x)
    else:
        return search(A[2], x)

# Calcola altezza/profondità dell'albero
def depth(A):
    if empty(A):
        return 0
    return max(depth(A[1]), depth(A[2])) + 1

# Calcola il bilancio del nodo (altezza sinistra - altezza destra)
def bil(A):
    if empty(A):
        return 0
    return depth(A[1]) - depth(A[2])

# Trova il valore minimo nell'albero
def findMin(A):
    if empty(A):
        return None
    if empty(A[1]):
        return A[0]
    return findMin(A[1])

# Trova il valore massimo nell'albero
def findMax(A):
    if empty(A):
        return None
    if empty(A[2]):
        return A[0]
    return findMax(A[2])

# Visita Preordine (Radice, Sinistra, Destra)
def prefix(A):
    result = []
    def prefixRec(node):
        if not empty(node):
            result.append(node[0])
            prefixRec(node[1])
            prefixRec(node[2])
    prefixRec(A)
    return result

# Visita Inordine (Sinistra, Radice, Destra)
def infix(A):
    result = []
    def infixRec(node):
        if not empty(node):
            infixRec(node[1])
            result.append(node[0])
            infixRec(node[2])
    infixRec(A)
    return result

# Visita Postordine (Sinistra, Destra, Radice)
def postfix(A):
    result = []
    def postfixRec(node):
        if not empty(node):
            postfixRec(node[1])
            postfixRec(node[2])
            result.append(node[0])
    postfixRec(A)
    return result

# Inserimento ricorsivo nel BST
def insert(A, x):
    if empty(A):
        return addNode(x)
    if x < A[0]:
        A[1] = insert(A[1], x)
    else:
        A[2] = insert(A[2], x)
    return A

# Rotazione a destra
def rightRotate(A):
    if empty(A) or empty(A[1]):
        return A
    B = A[1]
    A[1] = B[2]
    B[2] = A
    return B

# Rotazione a sinistra
def leftRotate(A):
    if empty(A) or empty(A[2]):
        return A
    B = A[2]
    A[2] = B[1]
    B[1] = A
    return B

# Bilancia un albero AVL
def balance(A):
    if empty(A):
        return A
    
    balance = bil(A)
    
    # Caso LL: bilancio > 1 e figlio sinistro compatto
    if balance > 1 and bil(A[1]) >= 0:
        A = rightRotate(A)
    # Caso RR: bilancio < -1 e figlio destro compatto
    elif balance < -1 and bil(A[2]) <= 0:
        A = leftRotate(A)
    # Caso LR: bilancio > 1 e figlio sinistro sbilanciato a destra
    elif balance > 1 and bil(A[1]) < 0:
        A[1] = leftRotate(A[1])
        A = rightRotate(A)
    # Caso RL: bilancio < -1 e figlio destro sbilanciato a sinistra
    elif balance < -1 and bil(A[2]) > 0:
        A[2] = rightRotate(A[2])
        A = leftRotate(A)
    
    return A

# Inserimento con bilanciamento AVL
def insertAVL(A, x):
    if empty(A):
        return addNode(x)
    if x < A[0]:
        A[1] = insertAVL(A[1], x)
    else:
        A[2] = insertAVL(A[2], x)
    return balance(A)

# Soppressione ricorsiva dal BST
def delete(A, x):
    if empty(A):
        return A
    
    if x < A[0]:
        A[1] = delete(A[1], x)
    elif x > A[0]:
        A[2] = delete(A[2], x)
    else:
        # Nodo trovato - tre casi
        # Caso 1: no figli (foglia)
        if empty(A[1]) and empty(A[2]):
            return []
        # Caso 2: solo figlio destro
        elif empty(A[1]):
            return A[2]
        # Caso 3: solo figlio sinistro
        elif empty(A[2]):
            return A[1]
        # Caso 4: due figli - sostituisci con successore (min del sottoalbero destro)
        else:
            minDx = findMin(A[2])
            A[0] = minDx
            A[2] = delete(A[2], minDx)
    
    return A

# Soppressione con bilanciamento AVL
def deleteAVL(A, x):
    A = delete(A, x)
    if not empty(A):
        A = balance(A)
    return A
#Il bilanciamento è meglio averlo nel nodo per non calcolarlo ogni volta

# TESTING
#L = [4, 2, 5, 8, 3, 1, 7, 6]
L = [5, 2, 3, 6, 1]
T = []

print("=== Inserimento semplice (BST) ===")
for x in L:
    T = insert(T, x)
    print(f"Inserito {x}: {T}")

print("\n=== Visite dell'albero ===")
print(f"Preordine: {prefix(T)}")
print(f"Inordine: {infix(T)}")
print(f"Postordine: {postfix(T)}")

print("\n=== Ricerca ===")
print(f"Ricerca 5: {search(T, 5)}")
print(f"Ricerca 10: {search(T, 10)}")

print("\n=== Altezza e bilancio ===")
print(f"Altezza: {depth(T)}")
print(f"Bilancio radice: {bil(T)}")

print("\n=== Minimo e massimo ===")
print(f"Minimo: {findMin(T)}")
print(f"Massimo: {findMax(T)}")

print("\n=== Cancellazione ===")
T = delete(T, 1)
print(f"Dopo eliminazione di 1: {infix(T)}")
T = delete(T, 4)
print(f"Dopo eliminazione di 4 (radice): {infix(T)}")

print("\n=== Albero AVL (bilanciato) ===")
T_avl = []
for x in L:
    T_avl = insertAVL(T_avl, x)
print(f"Inordine AVL: {infix(T_avl)}")
print(f"Altezza AVL: {depth(T_avl)}")
print(f"Bilancio radice AVL: {bil(T_avl)}")
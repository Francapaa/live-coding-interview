
""" ORDENAR UN STACK DE FORMA EN QUE LOS ELEMENTOS MAS PEQUEÑOS QUEDEN EN LA PARTE SUPERIOR DEL STACK    """


def sort (stackRecieve: []) -> [] | None:
    sortedStack = []
    if not stackRecieve: 
        return None


    while stackRecieve:
     currentValue = stackRecieve.pop()
     while sortedStack and currentValue < sortedStack[-1]:
        stackRecieve.append(sortedStack.pop())
     sortedStack.append(currentValue)

    return sortedStack

print("STACK A PASAR: ", [1,4,5,2])
stackDevuelto = sort([1,4,5,2])
print("STACK ORDENADO: ", stackDevuelto)
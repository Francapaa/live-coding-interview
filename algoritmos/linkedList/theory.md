# Linked List (Lista Enlazada)

## ¿Qué es una Linked List?

Una **Linked List** (lista enlazada) es una estructura de datos lineal donde cada elemento (nodo) contiene:
- Un **valor** (data)
- Un **puntero** (referencia) al siguiente nodo

A diferencia de los arrays, los nodos no están almacenados en posiciones contiguas de memoria.

## Estructura del Código

### Node
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```
Cada nodo almacena un valor y una referencia al siguiente nodo (inicialmente `None`).

### SingleLinkedList
```python
class SingleLinkedList:
    def __init__(self):
        self.head = None
```
La lista mantiene una referencia al primer nodo (`head`).

## Operaciones

### appendToTail(value)
Agrega un nuevo nodo al final de la lista:
1. Si la lista está vacía, el nuevo nodo se convierte en `head`
2. Si no, recorre la lista hasta el último nodo y enlaza el nuevo nodo

**Complejidad:** O(n) - debe recorrer toda la lista

### deleteNode(value)
Elimina el primer nodo que contenga el valor especificado:
1. Si el nodo a eliminar es el `head`, mueve `head` al siguiente nodo
2. Recorre la lista buscando el nodo cuyo `next` contenga el valor y lo "salta"

**Complejidad:** O(n)

### print()
Recorre la lista e imprime cada valor, mostrando la estructura visual "-> valor".

**Complejidad:** O(n)

## Complejidad Temporal

| Operación | Complejidad |
|-----------|-------------|
| Insertar al final | O(n) |
| Insertar al inicio | O(1) |
| Eliminar | O(n) |
| Buscar | O(n) |
| Acceso por índice | O(n) |

## Ventajas vs Arrays

- **Ventaja:** Inserción/eliminación O(1) al inicio (no requiere mover elementos)
- **Desventaja:** No acceso aleatorio (debe recorrer desde head)
- **Ventaja:** Tamaño dinámico (no requiere saber el tamaño)
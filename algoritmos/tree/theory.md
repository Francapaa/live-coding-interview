# Teoría de Árboles

## 1. Concepto

Un **árbol** es una estructura de datos jerárquica no lineal que consiste en nodos conectados por aristas. Cada árbol tiene un **nodo raíz** a partir del cual se ramifica hacia abajo.

### Terminología básica

- **Nodo raíz (Root)**: El nodo superior del árbol, no tiene padre
- **Nodo padre (Parent)**: Nodo que tiene nodos hijos debajo
- **Nodo hijo (Child)**: Nodo conectado a un padre
- **Nodos hermanos (Siblings)**: Nodos que comparten el mismo padre
- **Nodo hoja (Leaf)**: Nodo sin hijos (nodo terminal)
- **Nodo interno**: Nodo que tiene al menos un hijo
- **Profundidad/Nivel**: Distancia desde la raíz hasta un nodo (la raíz tiene profundidad 0)
- **Altura**: Longitud del camino más largo desde la raíz hasta una hoja
- **Subárbol**: Cualquier nodo junto con todos sus descendientes
- **Grado**: Número de hijos de un nodo

## 2. Tipos de Árboles

### Árbol Binario
Cada nodo tiene máximo 2 hijos (izquierdo y derecho).

### Árbol Binario de Búsqueda (BST)
- Binary Search Tree
- Todos los nodos en el subárbol izquierdo son menores que la raíz
- Todos los nodos en el subárbol derecho son mayores que la raíz
- Se aplica recursivamente a ambos subárboles

### Árbol AVL
- Árbol BST balanceado
- La diferencia de altura entre subárboles izquierdo y derecho es a lo sumo 1
- Requiere rotaciones para mantener el balance

### Árbol B (B-Tree)
- Óptimo para sistemas que leen/escriben grandes bloques de datos
- Común en bases de datos y sistemas de archivos
- Nodos pueden tener más de 2 hijos

### Trie (Árbol de prefijo)
- Estructura usada para almacenar y buscar Strings eficientemente
- Cada nodo representa un carácter
- Útil para autocomplete y búsqueda de palabras

### Heap (Montículo)
- Árbol binario completo donde cada nodo es mayor (max-heap) o menor (min-heap) que sus hijos
- Usado en priority queues y algoritmos de ordenamiento

## 3. Representación en Memoria

### Representación con Nodos Enlazados (Linked Nodes)

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # o left, right para árbol binario
```

**Ventajas:**
- Uso dinámico de memoria
- Representación intuitiva
- Inserción/eliminación eficiente

**Desventajas:**
- Overhead de punteros
- No es cache-friendly

### Representación en Array

Para árboles binarios completos, se puede usar un array donde:
- Índice 0: raíz
- Para nodo en índice i:
  - Hijo izquierdo: 2i + 1
  - Hijo derecho: 2i + 2
  - Padre: floor((i - 1) / 2)

**Ventajas:**
- No requiere punteros
- Mejor cache locality

**Desventajas:**
- Desperdicio de espacio si el árbol no está completo
- Tamaño fijo

## 4. Recorridos (Traversals)

### DFS (Depth-First Search) - Búsqueda en Profundidad

#### In-Order (Inorden)
```
Izquierda -> Raíz -> Derecha
```
Usado en BST para obtener elementos en orden ascendente.

#### Pre-Order (Preorden)
```
Raíz -> Izquierda -> Derecha
```
Usado para copiar/serializar árboles.

#### Post-Order (Postorden)
```
Izquierda -> Derecha -> Raíz
```
Usado para eliminar nodos o evaluar expresiones.

### BFS (Breadth-First Search) - Búsqueda en Anchura

#### Level-Order
Explora nivel por nivel de izquierda a derecha.
Usa una cola (queue) para implementar.

## 5. Operaciones Básicas

### Búsqueda

```
search(node, target):
    if node is null:
        return null
    if node.value == target:
        return node
    if target < node.value:
        return search(node.left, target)
    else:
        return search(node.right, target)
```

### Inserción (en BST)

```
insert(node, value):
    if node is null:
        return new TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node
```

### Eliminación (en BST)

Tres casos:
1. Nodo hoja: simplemente remover
2. Un hijo: reemplazar con el hijo
3. Dos hijos: reemplazar con el sucesor in-order (menor del subárbol derecho) o predecessor (mayor del subárbol izquierdo)

### Recorridos

Los 4 tipos principales:
- In-order: Left → Root → Right
- Pre-order: Root → Left → Right
- Post-order: Left → Right → Root
- Level-order: Por niveles (BFS)

## 6. Complejidad Algorítmica

### Árbol Binario (genérico)

| Operación | Promedio | Peor caso |
|-----------|----------|-----------|
| Búsqueda  | O(n)     | O(n)      |
| Inserción | O(n)     | O(n)      |
| Eliminación| O(n)    | O(n)      |

### BST (Balanceado)

| Operación | Promedio | Peor caso |
|-----------|----------|-----------|
| Búsqueda  | O(log n) | O(n)      |
| Inserción | O(log n) | O(n)      |
| Eliminación| O(log n)| O(n)      |

### AVL (Balanceado automáticamente)

| Operación | Promedio | Peor caso |
|-----------|----------|-----------|
| Búsqueda  | O(log n) | O(log n)  |
| Inserción | O(log n) | O(log n)  |
| Eliminación| O(log n)| O(log n)  |

### Espacio: O(n) para todas las implementaciones



## Resumen Visual de Recorridos

```
        1
       / \
      2   3
     / \   \
    4   5   6

In-order:   4 → 2 → 5 → 1 → 3 → 6
Pre-order:  1 → 2 → 4 → 5 → 3 → 6
Post-order: 4 → 5 → 2 → 6 → 3 → 1
Level-order: 1 → 2 → 3 → 4 → 5 → 6
```
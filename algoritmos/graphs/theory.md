# Teoría de Grafos

## 1. Introducción

Un grafo es una estructura de datos matemática compuesta por vertices (también llamados nodos) y aristas (también llamadas arcos o bordes) que conectan pares de vertices. Los grafos son fundamentales en ciencias de la computación porque permiten modelar relaciones entre objetos de manera eficiente. Se utilizan en redes sociales para representar conexiones entre usuarios, en sistemas de navegación para encontrar rutas óptimas entre ubicaciones, en análisis de dependencias para determinar el orden de ejecución de tareas, y en muchos otros dominios donde las relaciones entre entidades son importantes.

La teoría de grafos proporciona las herramientas conceptuales y algorítmicas necesarias para resolver problemas como encontrar el camino más corto entre dos puntos, determinar si un grafo está conectado, identificar ciclos, y optimizar flujos en redes. La diversidad de aplicaciones hace que el estudio de grafos sea esencial para cualquier programador o científico de datos.

## 2. Terminología Fundamental

### 2.1 Componentes Básicos

Un **vértice** (o nodo) es la unidad fundamental de un grafo. Representa una entidad individual dentro del grafo. Por ejemplo, en un mapa de ciudades, cada ciudad sería un vértice. Cada vértice puede tener propiedades adicionales como un identificador único, un peso, o metadatos asociados.

Una **arista** (o arco, borde) es una conexión entre dos vértices. Las aristas representan las relaciones entre las entidades. En el ejemplo del mapa, una arista representaría una carretera que conecta dos ciudades. Las aristas pueden tener dirección (en grafos dirigidos) o no (en grafos no dirigidos), y pueden tener un peso asociado que representa una métrica como distancia, costo o tiempo.

Un **adyacente** es un vértice que está conectado directamente a otro vértice mediante una arista. Si el vértice A está conectado al vértice B por una arista, entonces A es adyacente a B y viceversa (en grafos no dirigidos). El grado de un vértice es el número de aristas incidentes en él. En grafos dirigidos, se distingue entre grado de entrada (número de aristas que llegan al vértice) y grado de salida (número de aristas que salen del vértice).

### 2.2 Caminos y Ciclos

Un **camino** es una secuencia de vértices donde cada par de vértices consecutivos está conectado por una arista. La longitud de un camino es el número de aristas que contiene. Un camino simple es aquel que no repite vértices (excepto posiblemente el vértice inicial y final en un ciclo). El camino más corto entre dos vértices es aquel con el menor número de aristas o, en grafos ponderados, la menor suma de pesos.

Un **ciclo** es un camino que comienza y termina en el mismo vértice. Un ciclo simple es aquel que no repite vértices (excepto el inicial y final). Los grafos que no contienen ciclos se llaman grafos acíclicos. Un grafo no dirigido que es sowohl conexo como acíclico es un árbol.

### 2.3 Propiedades Globales

Un grafo es **conexo** si existe un camino entre cada par de vértices. En un grafo conexo, se puede llegar desde cualquier vértice a cualquier otro vértice siguiendo las aristas. Un grafo no conexo está compuesto por uno o más componentes conexos, donde cada componente es un subgrafo conexo máximo.

Un grafo es **completo** si existe una arista entre cada par de vértices. Un grafo completo con n vértices tiene n(n-1)/2 aristas (en grafos no dirigidos). Estos grafos representan el caso donde todas las entidades están directamente relacionadas.

## 3. Tipos de Grafos

### 3.1 Grafos Dirigidos y No Dirigidos

En un **grafo no dirigido**, las aristas no tienen dirección. La relación entre dos vértices es simétrica: si existe una arista entre A y B, se puede viajar de A a B y de B a A. Las redes sociales donde las conexiones son mutuas (como Facebook) se modelan como grafos no dirigidos.

En un **grafo dirigido** (dígrafo), cada arista tiene una dirección específica. Se distingue entre aristas que van de un vértice a otro. Las relaciones asimétricas como "sigue" en Twitter o las dependencias en un sistema de archivos se modelan como grafos dirigidos. En este contexto, se habla de sucesores (vértices alcanzables desde un vértice dado) y predecesores (vértices que pueden alcanzar un vértice dado).

### 3.2 Grafos Ponderados y No Ponderados

En un **grafo no ponderado**, todas las aristas tienen el mismo peso o costo. El costo de un camino es simplemente el número de aristas. Estos grafos son útiles cuando la única información relevante es la existencia de una conexión.

En un **grafo ponderado**, cada arista tiene un peso asociado que representa una métrica como distancia, tiempo, costo o capacidad. El costo de un camino es la suma de los pesos de sus aristas. Los sistemas de navegación GPS utilizan grafos ponderados donde el peso representa la distancia o tiempo de viaje entre intersecciones.

### 3.3 Otras Clasificaciones

Un grafo **estival** es un grafo no dirigido donde los vértices se pueden colorear con k colores sin que dos vértices adyacentes compartan el mismo color. El número mínimo de colores necesarios se llama número cromático. Este concepto tiene aplicaciones en asignación de frecuencias, horarios y register allocation.

Un grafo **bipartito** es un grafo no dirigido cuyos vértices se pueden dividir en dos conjuntos disjointos tales que todas las aristas conectan vértices de conjuntos diferentes. Un ejemplo clásico es el problema de asignar trabajadores a trabajos donde cada trabajador puede realizar ciertos trabajos.

## 4. Representación de Grafos

### 4.1 Matriz de Adyacencia

La matriz de adyacencia es una representación tabular donde cada fila y columna representa un vértice. La celda (i, j) indica si existe una arista entre los vértices i y j. Para grafos no ponderados, typically se usa 1 para indicar presencia de arista y 0 para ausencia. Para grafos ponderados, se almacena el peso o infinito si no hay arista.

```python
class GraphAdjacencyMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight  # grafo no dirigido
    
    def has_edge(self, u, v):
        return self.matrix[u][v] > 0
    
    def get_neighbors(self, v):
        return [i for i in range(self.V) if self.matrix[v][i] > 0]
```

La complejidad espacial es O(V²), lo cual puede ser prohibitivo para grafos dispersos con muchos vértices pero pocas aristas. Sin embargo, la verificación de adyacencia es O(1), lo cual puede ser ventajoso en ciertos algoritmos.

### 4.2 Lista de Adyacencia

La lista de adyacencia almacena para cada vértice la lista de sus vecinos. Esta representación es más eficiente en espacio para grafos dispersos, usando O(V + E) donde E es el número de aristas. Es la representación más común en la práctica.

```python
from collections import defaultdict

class GraphAdjacencyList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=None):
        self.graph[u].append((v, weight))
        # para grafo no dirigido, descomenta la siguiente línea
        # self.graph[v].append((u, weight))
    
    def add_undirected_edge(self, u, v, weight=None):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def get_neighbors(self, v):
        return self.graph[v]
    
    def vertices(self):
        return list(self.graph.keys())
```

La verificación de adyacencia tiene complejidad O(grado(v)) = O(V) en el peor caso, pero el espacio total es proporcional al número de aristas reales.

## 5. Recorrido de Grafos

### 5.1 Búsqueda en Anchura (BFS)

La búsqueda en anchura explora el grafo nivel por nivel, visitando primero todos los vértices a distancia d del vértice de inicio antes de pasar a los vértices a distancia d+1. BFS utiliza una cola (FIFO) para procesar los vértices y un conjunto para marcar los vértices visitados.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# BFS también encuentra el camino más corto en grafos no ponderados
def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # no hay camino
```

La complejidad de tiempo de BFS es O(V + E) y la complejidad de espacio es O(V). BFS es útil para encontrar el camino más corto en grafos no ponderados, verificar si un grafo es bipartito, y realizar problemas de alcanzarabilidad.

### 5.2 Búsqueda en Profundidad (DFS)

DFS explora tan lejos como sea posible a lo largo de cada rama antes de retroceder. Utiliza una pila (explícitamente o mediante recursión) y un conjunto de visitados. DFS es especialmente útil para detectar ciclos, encontrar componentes fuertemente conexos, y realizar topological sorting.

```python
def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []
    
    visited.add(start)
    result.append(start)
    
    for neighbor, _ in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    
    return result

# Versión iterativa usando pila explícita
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # agregar vecinos en orden inverso para mantener consistencia
            neighbors = graph.get_neighbors(vertex)
            for neighbor, _ in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

DFS también puede ser utile para encontrar componentes fuertemente conexos mediante el algoritmo de Kosaraju o Tarjan, y para realizar ordenamiento topológico en grafos acíclicos dirigidos.

### 5.3 Aplicaciones del Recorrido

Una aplicación común es detectar si un grafo contiene ciclos. En grafos no dirigidos, un ciclo existe si durante DFS encontramos un vértice ya visitado que no es el padre del vértice actual. En grafos dirigidos, la detección de ciclos es más compleja y puede realizarse usando DFS con tres estados (no visitado, en progreso, completado).

```python
def has_cycle_undirected(graph):
    visited = set()
    
    def dfs(vertex, parent):
        visited.add(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            if dfs(neighbor, vertex):
                return True
        
        return False
    
    for vertex in graph.vertices():
        if vertex not in visited:
            if dfs(vertex, -1):
                return True
    
    return False
```

Otra aplicación es el ordenamiento topológico, que produce un orden lineal de los vértices de un grafo acíclico dirigido donde para cada arista dirigida (u, v), u aparece antes que v en el orden. Esto es útil para scheduling de tareas con dependencias.

## 6. Algoritmos de Grafos Importantes

### 6.1 Algoritmo de Dijkstra

El algoritmo de Dijkstra encuentra el camino más corto desde un vértice fuente a todos los demás vértices en un grafo ponderado con pesos no negativos. Utiliza una cola de prioridad (heap) para seleccionar siempre el vértice no procesado con la distancia mínima conocida.

```python
import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph.vertices()}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, vertex = heapq.heappop(pq)
        
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        for neighbor, weight in graph.get_neighbors(vertex):
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return distances
```

La complejidad de tiempo es O((V + E) log V) usando un heap binario. Para grafos densos donde E ≈ V², esto es O(V² log V). Existen implementaciones optimizadas para casos específicos como grafos muy densos.

### 6.2 Algoritmo de Bellman-Ford

A diferencia de Dijkstra, Bellman-Ford puede manejar pesos negativos y detectar ciclos negativos. El algoritmo relaja todas las aristas V-1 veces, donde cada relajación examina todas las aristas del grafo.

```python
def bellman_ford(graph, start):
    distances = {v: float('inf') for v in graph.vertices()}
    distances[start] = 0
    
    vertices_list = list(graph.vertices())
    
    # V-1 iteraciones para relajar todas las aristas
    for _ in range(len(vertices_list) - 1):
        for u in vertices_list:
            for v, weight in graph.get_neighbors(u):
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Una iteración adicional para detectar ciclos negativos
    for u in vertices_list:
        for v, weight in graph.get_neighbors(u):
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return None  # ciclo negativo detectado
    
    return distances
```

La complejidad de tiempo es O(V E), lo cual es mayor que Dijkstra para grafos densos, pero la capacidad de manejar pesos negativos lo hace indispensable en ciertos contextos.

### 6.3 Algoritmo de Floyd-Warshall

Floyd-Warshall encuentra los caminos más cortos entre todos los pares de vértices. Es un algoritmo de programación dinámica que considera todos los vértices intermedios posibles.

```python
def floyd_warshall(graph):
    vertices = list(graph.vertices())
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    
    # inicializar matriz de distancias
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    # cargar las aristas
    for u in vertices:
        for v, weight in graph.get_neighbors(u):
            dist[index[u]][index[v]] = weight
    
    # algoritmo principal
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # convertir de vuelta a diccionario
    result = {}
    for i, u in enumerate(vertices):
        result[u] = {}
        for j, v in enumerate(vertices):
            result[u][v] = dist[i][j]
    
    return result
```

La complejidad de tiempo es O(V³) y la complejidad de espacio es O(V²). Es óptima para grafos densos con muchos vértices donde V es pequeño.

### 6.4 Algoritmo de Kruskal

Kruskal encuentra el árbol de expansión mínima (MST) para un grafo no dirigido ponderado. Funciona ordenando todas las aristas por peso y agregándolas una por una si no forman un ciclo.

```python
def kruskal(graph):
    parent = {v: v for v in graph.vertices()}
    rank = {v: 0 for v in graph.vertices()}
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(v1, v2):
        root1, root2 = find(v1), find(v2)
        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        return False
    
    # obtener todas las aristas con sus pesos
    edges = []
    for u in graph.vertices():
        for v, weight in graph.get_neighbors(u):
            edges.append((weight, u, v))
    
    edges.sort()
    
    mst = []
    for weight, u, v in edges:
        if union(u, v):
            mst.append((u, v, weight))
    
    return mst
```

Kruskal tiene complejidad O(E log E) = O(E log V). Es óptimo para grafos dispersos.

### 6.5 Algoritmo de Prim

Prim es otro algoritmo para encontrar el MST, pero crece el árbol desde un vértice fuente, agregando la arista de menor peso que conecta un vértice en el árbol a uno fuera de él.

```python
import heapq

def prim(graph, start):
    visited = {start}
    edges = []
    
    # agregar todas las aristas del vértice inicial
    pq = [(weight, start, v) for v, weight in graph.get_neighbors(start)]
    heapq.heapify(pq)
    
    while pq:
        weight, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        visited.add(v)
        edges.append((u, v, weight))
        
        for neighbor, w in graph.get_neighbors(v):
            if neighbor not in visited:
                heapq.heappush(pq, (w, v, neighbor))
    
    return edges
```

La complejidad de Prim es similar a Kruskal: O(E log V) con un heap binario. La elección entre Kruskal y Prim depende del tipo de grafo y la representación utilizada.

## 7. Grafos Dirigidos Acíclicos (DAG)

### 7.1 Ordenamiento Topológico

El ordenamiento topológico es una ordenación lineal de los vértices de un DAG donde cada vértice aparece antes que todos sus sucesores. Es útil para scheduling de tareas con dependencias.

```python
def topological_sort(graph):
    # calcular grados de entrada
    in_degree = {v: 0 for v in graph.vertices()}
    for u in graph.vertices():
        for v, _ in graph.get_neighbors(u):
            in_degree[v] += 1
    
    # inicializar cola con vértices de grado 0
    queue = [v for v in graph.vertices() if in_degree[v] == 0]
    result = []
    
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # si el resultado no incluye todos los vértices, hay un ciclo
    if len(result) != len(graph.vertices()):
        return None
    
    return result
```

La complejidad de tiempo es O(V + E). Si el grafo tiene un ciclo, el algoritmo retorna None.

### 7.2 Componentes Fuertemene Conexos

Un componente fuertemente conexo (SCC) es un subgrafo donde cada vértice puede alcanzar todos los demás vértices del componente. El algoritmo de Kosaraju utiliza dos pasadas de DFS.

```python
def kosaraju_scc(graph):
    # primera pasada: DFS para obtener orden de finish
    visited = set()
    finish_order = []
    
    def dfs1(v):
        visited.add(v)
        for neighbor, _ in graph.get_neighbors(v):
            if neighbor not in visited:
                dfs1(neighbor)
        finish_order.append(v)
    
    for v in graph.vertices():
        if v not in visited:
            dfs1(v)
    
    # crear grafo transpuesto
    transposed = GraphAdjacencyList()
    for u in graph.vertices():
        for v, w in graph.get_neighbors(u):
            transposed.add_edge(v, u, w)
    
    # segunda pasada: DFS en orden reverso
    visited.clear()
    sccs = []
    
    def dfs2(v):
        visited.add(v)
        component.append(v)
        for neighbor, _ in transposed.get_neighbors(v):
            if neighbor not in visited:
                dfs2(neighbor)
    
    for v in reversed(finish_order):
        if v not in visited:
            component = []
            dfs2(v)
            sccs.append(component)
    
    return sccs
```

Los SCCs tienen aplicaciones en análisis de dependencias, detección de ciclos, y compresión de grafos.

## 8. Algoritmo de A*

A* es un algoritmo de búsqueda informada que encuentra el camino más corto utilizando una heurística para guiar la búsqueda. Es una extensión de Dijkstra que incorpora información adicional sobre la estimación del costo restante.

```python
import heapq

def astar(graph, start, goal, heuristic):
    #heuristic(v) estima el costo de v al goal
    open_set = [(heuristic(start), start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            # reconstruir camino
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, weight in graph.get_neighbors(current):
            tentative_g = g_score[current] + weight
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # no hay camino
```

La heurística debe ser admisible (nunca overestimate el costo real) para garantizar optimalidad. A* es ampliamente utilizado en juegos, robótica y planificación de rutas.

## 9. Consideraciones Prácticas

### 9.1 Elección de Representación

La elección entre matriz de adyacencia y lista de adyacencia depende del tipo de grafo. Para grafos densos (E ≈ V²), la matriz de adyacencia puede ser más eficiente en tiempo de acceso. Para grafos dispersos (E << V²), la lista de adyacencia usa menos memoria y permite iterar sobre vecinos eficientemente.

### 9.2 Manejo de Grandes Grafos

Para grafos muy grandes que no caben en memoria, se utilizan técnicas como procesamiento externo, grafos comprimidos, y representaciones especializadas. Libraries como NetworkX (Python), GraphLab (C++), y Neo4j (base de datos de grafos) ofrecen implementaciones optimizadas.

### 9.3 Testing y Debugging

Al trabajar con grafos, es útil generar grafos de prueba con propiedades conocidas, visualizar el grafo para debugging, y verificar propiedades como conectividad, ciclos, y planaridad según corresponda al problema.
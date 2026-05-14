# Binary Search (Búsqueda Binaria)

## 1. Concepto

Binary Search es un algoritmo de búsqueda que encuentra la posición de un valor objetivo en un **array ordenado**. Funciona dividiendo repetidamente el intervalo de búsqueda por la mitad.

**Requisito fundamental:** El array debe estar ordenado.

## 2. Funcionamiento

1. Comparar el elemento objetivo con el elemento central del array
2. Si son iguales, retornar la posición
3. Si el objetivo es menor, buscar en la mitad izquierda
4. Si el objetivo es mayor, buscar en la mitad derecha
5. Repetir hasta encontrar el elemento o determinar que no existe

## 3. Implementación

### Iterativa

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # No encontrado
```

### Recursiva

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

## 4. Complejidad Algorítmica

| Métrica | Complejidad |
|---------|-------------|
| Tiempo (promedio) | O(log n) |
| Tiempo (peor caso) | O(log n) |
| Espacio (iterativo) | O(1) |
| Espacio (recursivo) | O(log n) por stack |

**¿Por qué O(log n)?** En cada iteración se reduce el tamaño del problema a la mitad.

## 5. Variaciones

### Lower Bound - Primera ocurrencia
Encontrar la primera posición donde aparece el valor.

```python
def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result
```

### Upper Bound - Última ocurrencia
Encontrar la última posición donde aparece el valor.

```python
def upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Buscar en Rotated Array
Array ordenado que fue rotado en algún punto.

```
[4, 5, 6, 7, 0, 1, 2]
```

## 6. Aplicaciones

- Búsqueda en datasets grandes
- Búsqueda en bases de datos indexadas
- Algoritmos de optimización (binary search en respuestas)
- Encontrar thresholds o límites
- Search en herramientas de versionado (git bisect)

## 7. Ejemplo Visual

```
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
Target: 23

Iteración 1: [2, 5, 8, 12, 16 | 23, 38, 56, 72, 91]
            mid=16 < 23 → buscar derecha

Iteración 2:              [| 23, 38, 56, 72, 91]
            mid=56 > 23 → buscar izquierda

Iteración 3:              [23 | 38]
            mid=23 == 23 → ¡Encontrado!

Índice: 5
```

## 8. Errores Comunes

1. **Olvidar verificar `left <= right`** - puede perder elementos
2. **Usar `(left + right) / 2`** - puede overflow en lenguajes con límites
3. **No actualizar límites correctamente** - usar `mid + 1` o `mid - 1`
4. **Aplicar en array no ordenado** - siempre verificar ordenamiento

## 9. Cuándo Usar Binary Search

- ✅ Array ordenado
- ✅ Búsqueda de elementos únicos
- ✅ Complejidad O(log n) necesaria
- ✅ Acceso aleatorio eficiente (array, no linked list)

- ❌ Array pequeño (overhead no justifica)
- ❌ Datos no ordenados (ordenar primero o usar otra estructura)
- ❌ Solo acceso secuencial disponible
# Strings y Hash/Set

## El Problema: Caracteres Únicos

Dada una cadena de texto, determinar si todos sus caracteres son únicos (sin repetirse).

**Ejemplos:**
- `"abcde"` → `True` (todos distintos)
- `"abcded"` → `False` (la 'd' se repite)

## Solución 1: Fuerza Bruta (isUnique)

```python
def isUnique(text: str) -> bool:
    for i, char1 in enumerate(text):
        for j, char2 in enumerate(text):
            if char1 == char2 and i != j:
                return False
    return True
```

Compara cada caracter con todos los demás usando dos bucles anidados.

**Complejidad:** O(n²) - tiempo cuadrático
**Espacio:** O(1) - solo usa variables simples

## ¿Qué es un Hash/Set?

Un **Set** (conjunto) es una estructura de datos que:
- **Almacena elementos únicos** - no permite duplicados
- **Búsqueda O(1)** - promedio constante

Internamente usa una **tabla hash**:
1. Convierte la clave (caracter) en un índice usando una función hash
2. Almacena el valor en esa posición
3. La búsqueda es casi instantánea porque calcula directamente la posición

### Ejemplo visual:
```
Buscarlo 'a' → función hash → índice 3 → O(1) encontrarlo
```

## Solución 2: Hash/Set (isUniqueHash)

```python
def isUniqueHash(text: str) -> bool:
    NUMBERS_OF_CHARS = 128
    if len(text) > NUMBERS_OF_CHARS:
        return False
    Characters = set()
    for c in text:
        if c in Characters:
            return False
        Characters.add(c)
    return True
```

**Complejidad:** O(n) - solo un bucle
**Espacio:** O(n) - almacena hasta n caracteres

### Optimización adicional:
- Si la cadena tiene más de 128 caracteres (ASCII), forzosamente hay repetición
- Retorna `False` inmediatamente sin procesar

## Comparación de Complejidad

| Solución | Tiempo | Espacio |
|----------|--------|---------|
| Fuerza Bruta | O(n²) | O(1) |
| Hash/Set | O(n) | O(n) |

## Conclusión

La solución con Hash/Set es significativamente más eficiente para strings largos:
- **n = 1000**: 1,000,000 comparaciones vs 1,000 operaciones
- Trade-off: usa más memoria pero gana en velocidad

## Aplicaciones reales de Hash/Set

- Validación de datos únicos (emails, usernames)
- Detección de duplicados en grandes volúmenes de datos
- Implementación de caches
- Búsqueda rápida en bases de datos
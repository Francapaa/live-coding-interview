# Fix The Bug - Guía de Errores Comunes

## 1. JavaScript: Métodos de Array (Funcionales)

Priorizá siempre los métodos que no mutan el array original.

| Método | Uso Principal | Retorno |
|--------|---------------|---------|
| `.map()` | Transformar cada elemento | Un nuevo array del mismo largo |
| `.filter()` | Descartar elementos según una condición | Un nuevo array (puede ser más corto) |
| `.reduce()` | Acumular el array en un solo valor (suma, objeto, etc) | El valor acumulado |
| `.find()` | Buscar el primer elemento que cumpla la condición | El elemento o undefined |
| `.some()` | ¿Al menos uno cumple la condición? | true / false |
| `.every()` | ¿Todos cumplen la condición? | true / false |

### Ojo con los "Destructores"

```javascript
const copy = [...original].sort();
```

Siempre cloná con el spread operator `[...]` antes de usar `.sort()` o `.reverse()`, porque estos sí modifican el original.

---

## 2. JavaScript: Manejo de Asincronía

En una prueba de 30-60 min, el 90% de los errores son por promesas mal manejadas.

### El patrón async/await

```javascript
const fetchData = async () => {
  try {
    const response = await fetch('https://api.ejemplo.com/data');
    if (!response.ok) throw new Error('Network error');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
};
```

### Ejecución en paralelo vs. Secuencial

**Paralelo (Más rápido):** Usalo si las llamadas no dependen entre sí.

```javascript
const [users, posts] = await Promise.all([getUsers(), getPosts()]);
```

**Secuencial (Cuidado con los loops):**

MAL:
```javascript
arr.forEach(async (item) => await api(item))
// El forEach no espera
```

BIEN:
```javascript
for (const item of arr) {
  await api(item);
}
```

---

## 3. Python: Lo fundamental para Tests

Python es excelente para manipular datos rápido. Estos "tricks" te ahorran mucho código.

### List & Dictionary Comprehensions

```python
# Crear lista de cuadrados de números pares
squares = [x**2 for x in range(10) if x % 2 == 0]

# Crear un mapa de id:nombre
user_map = {u['id']: u['name'] for u in users}
```

### Manejo seguro de Diccionarios

Evitá el KeyError. Usá siempre `.get()`:

```python
value = my_dict.get('key', 'default_value')  # Si no existe, devuelve el default
```

### F-Strings (Formateo rápido)

```python
print(f"User {name} has {len(items)} items.")
```

### Slicing (Trucos de strings/listas)

```python
lista[::-1]   # Invierte la lista
lista[:3]     # Primeros 3 elementos
lista[-1]     # Último elemento
```

---

## 4. Los 5 Bugs Clásicos

### Bug 1: El forEach Asincrónico (Clásico)

**Problema:** Se intenta procesar una lista de IDs llamando a una API, pero el código no espera a que terminen.

```javascript
// ❌ CÓDIGO CON BUG
const processUsers = (ids) => {
  const results = [];
  
  ids.forEach(async (id) => {
    const user = await fetchUser(id);  // La función sigue de largo sin esperar
    results.push(user);
  });

  return results;  // Devuelve [] (vacío) porque el forEach no es awaitable
};

// ✅ SOLUCIÓN
const processUsers = async (ids) => {
  return await Promise.all(ids.map(id => fetchUser(id)));
};
```

---

### Bug 2: La Referencia de Objetos (JS/Python)

**Problema:** Modificar un objeto que fue pasado por referencia, afectando al original sin querer.

**JavaScript:**
```javascript
// ❌ CÓDIGO CON BUG
const updatePrice = (product, newPrice) => {
  const updated = product; 
  updated.price = newPrice;  // Esto modifica el objeto original fuera de la función
  return updated;
};

// ✅ SOLUCIÓN
const updatePrice = (product, newPrice) => {
  return { ...product, price: newPrice };  // Clonar usando Spread Operator
};
```

**Python (Mutable Default Argument):**
```python
# ❌ CÓDIGO CON BUG
def add_item(item, items=[]):  # La lista [] se crea UNA sola vez y persiste
    items.append(item)
    return items

# ✅ SOLUCIÓN
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

### Bug 3: "Perder el Contexto" (this)

**Problema:** Muy común si te piden algo con clases o componentes antiguos.

```javascript
// ❌ CÓDIGO CON BUG
class Timer {
  constructor() {
    this.seconds = 0;
  }
  start() {
    setInterval(function() {
      this.seconds++;  // 'this' aquí es el objeto global/window, no la clase
    }, 1000);
  }
}

// ✅ SOLUCIÓN
class Timer {
  constructor() {
    this.seconds = 0;
  }
  start() {
    setInterval(() => {
      this.seconds++;  // Arrow function preserva el 'this' del contexto padre
    }, 1000);
  }
}
```

---

### Bug 4: 0 o "" (Falsy Values)

**Problema:** Validar datos de forma que el número cero o un string vacío se traten como errores.

```javascript
// ❌ CÓDIGO CON BUG
const getLength = (text) => {
  if (!text) return "No text provided";  // Si text es "", devuelve el error
  return text.length;
};

// ✅ SOLUCIÓN
const getLength = (text) => {
  if (text === undefined || text === null) return "No text provided";
  return text.length;
};
```

---

### Bug 5: Concurrencia en Python (FastAPI/Scripts)

**Problema:** Bloquear el event loop por no usar await o no definir la función como async.

```python
# ❌ CÓDIGO CON BUG
import time

async def get_data():
    time.sleep(5)  # Esto congela TODO el servidor, no solo esta función
    return {"status": "ok"}

# ✅ SOLUCIÓN
import asyncio

async def get_data():
    await asyncio.sleep(5)  # Esto libera el hilo para otras peticiones
    return {"status": "ok"}
```

---

## 5. Checklist de Debugging

- [ ] ¿El array original se está mutando accidentalmente?
- [ ] ¿Las promesas están siendo correctamente awaited?
- [ ] ¿Se está usando el `this` correcto en callbacks?
- [ ] ¿Los falsy values (0, "", false) están siendo validados correctamente?
- [ ] ¿Los objetos pasan por referencia y se modifican sin querer?
- [ ] ¿Las funciones async usan `await` correctamente?
- [ ] ¿Se están usando tipos mutables como valores por defecto en Python?
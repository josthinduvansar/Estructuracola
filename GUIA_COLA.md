# 📚 GUÍA COMPLETA DE COLAS

## ¿Qué es una Cola?

Una **cola** es una estructura de datos que sigue el principio **FIFO** (First In First Out - Primero Entra, Primero Sale). 

### Analogía del Mundo Real
Imagina una fila en un banco:
- Los clientes llegan y se forman en la fila (encolar)
- El cliente del frente es atendido primero (desencolar)
- Un nuevo cliente llega se pone al final de la fila

```
Frente                          Final
  ↓                             ↓
[Cliente1] → [Cliente2] → [Cliente3] → [Nuevo Cliente]
```

---

## Características Principales

| Característica | Descripción |
|---|---|
| **Inserción** | Siempre al final (enqueue) |
| **Eliminación** | Siempre al frente (dequeue) |
| **Acceso** | Solo el frente es accesible |
| **Orden** | FIFO (Primero Entra, Primero Sale) |

---

## Operaciones Básicas

### 1. **ENCOLAR (Enqueue)**
Agregar un elemento al final de la cola

```python
cola.encolar(5)
cola.encolar(10)
cola.encolar(15)
# Cola: [5, 10, 15]
```

### 2. **DESENCOLAR (Dequeue)**
Remover y retornar el primer elemento

```python
elemento = cola.desencolar()  # Retorna 5
# Cola: [10, 15]
```

### 3. **FRENTE**
Ver el primer elemento sin removerlo

```python
primero = cola.frente()  # Retorna 10
# Cola sigue siendo: [10, 15]
```

### 4. **ESTA VACÍA**
Verificar si la cola no tiene elementos

```python
if cola.esta_vacia():
    print("La cola está vacía")
```

### 5. **TAMAÑO**
Contar cuántos elementos hay

```python
cantidad = cola.tamaño()  # Retorna 2
```

---

## Complejidad de Operaciones

### Implementación con Lista (Array)
| Operación | Complejidad | Razón |
|---|---|---|
| Encolar | O(1) | Agregar al final |
| Desencolar | O(n) | Remover del inicio |
| Frente | O(1) | Acceso directo |
| Está vacía | O(1) | Verificación simple |
| Tamaño | O(1) | Contador |

### Implementación con Lista Enlazada
| Operación | Complejidad | Razón |
|---|---|---|
| Encolar | O(1) | Apuntar al final |
| Desencolar | O(1) | Cambiar referencia frente |
| Frente | O(1) | Acceso al nodo frente |
| Está vacía | O(1) | Verificación simple |
| Tamaño | O(1) | Contador |

---

## Ejemplos de Uso

### Ejemplo 1: Cola de Impresión
```python
cola_impresion = Cola()

# Documentos llegan para imprimir
cola_impresion.encolar("Documento1.pdf")
cola_impresion.encolar("Documento2.pdf")
cola_impresion.encolar("Documento3.pdf")

# La impresora procesa uno por uno
while not cola_impresion.esta_vacia():
    documento = cola_impresion.desencolar()
    print(f"Imprimiendo: {documento}")
```

### Ejemplo 2: Llamadas Telefónicas
```python
cola_llamadas = Cola()

# Llamadas entrantes
cola_llamadas.encolar("Llamada 1")
cola_llamadas.encolar("Llamada 2")
cola_llamadas.encolar("Llamada 3")

# Atender llamadas en orden
while not cola_llamadas.esta_vacia():
    llamada = cola_llamadas.desencolar()
    print(f"Atendiendo: {llamada}")
```

### Ejemplo 3: Procesar Tareas
```python
tareas = Cola()

# Agregar tareas
for i in range(1, 6):
    tareas.encolar(f"Tarea {i}")

# Ejecutar tareas secuencialmente
while not tareas.esta_vacia():
    tarea = tareas.desencolar()
    print(f"Ejecutando: {tarea}")
```

---

## Ventajas y Desventajas

### ✅ Ventajas
- Simple de entender e implementar
- Eficiente para procesamiento secuencial
- Útil para simular procesos del mundo real
- Garantiza orden FIFO

### ❌ Desventajas
- Acceso limitado (solo frente y final)
- No es eficiente para búsquedas
- No permite acceso aleatorio
- Con arrays, desencolar es O(n)

---

## Ejercicios Propuestos

### Nivel Básico
1. Crear una cola y encolar 5 números
2. Desencolar todos los elementos
3. Verificar si la cola está vacía

### Nivel Intermedio
1. Invertir el orden de una cola
2. Contar elementos mayores que un valor
3. Filtrar solo números pares

### Nivel Avanzado
1. Mezclar dos colas intercalando elementos
2. Encontrar el elemento máximo
3. Implementar cola con prioridades

---

## Diferencias: Cola vs Pila

| Cola | Pila |
|---|---|
| FIFO | LIFO |
| Encolar al final | Apilar al tope |
| Desencolar del frente | Desapilar del tope |
| Ej: Fila en banco | Ej: Navegador web |

---

## Archivos en Este Proyecto

1. **cola.py** - Implementación básica de cola
2. **cola_enlazada.py** - Implementación con nodos
3. **ejercicio_principal.py** - Ejercicios ejemplificados
4. **ejercicios_practicos.py** - 8 ejercicios adicionales
5. **GUIA_COLA.md** - Esta guía

---

## Cómo Ejecutar

```bash
# Ejecutar ejercicios principales
python ejercicio_principal.py

# Ejecutar ejercicios prácticos
python ejercicios_practicos.py

# Probar cola enlazada
python cola_enlazada.py
```

---

## Conclusión

Las colas son una estructura fundamental en programación que permite modelar procesos secuenciales y garantiza que los elementos se procesen en orden. Dominar las colas es esencial para entender estructuras más complejas como grafos y algoritmos de búsqueda por amplitud.

**Recuerda:** En una cola, el primero en entrar es el primero en salir (FIFO) ⏳

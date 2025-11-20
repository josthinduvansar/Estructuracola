"""
Implementación de una Cola usando Nodos (Lista Enlazada)
Esta es una implementación más eficiente que usa referencias en lugar de arrays
"""

class Nodo:
    """Representa un nodo en la cola enlazada"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ColaEnlazada:
    """
    Implementación de Cola usando lista enlazada
    Ventajas: Más eficiente en desencolar (O(1) vs O(n))
    """
    
    def __init__(self):
        """Inicializa una cola enlazada vacía"""
        self.frente_nodo = None
        self.final_nodo = None
        self._tamaño = 0
    
    def encolar(self, dato):
        """Agrega un elemento al final de la cola"""
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.frente_nodo = nuevo_nodo
            self.final_nodo = nuevo_nodo
        else:
            self.final_nodo.siguiente = nuevo_nodo
            self.final_nodo = nuevo_nodo
        
        self._tamaño += 1
    
    def desencolar(self):
        """Remueve y retorna el primer elemento"""
        if self.esta_vacia():
            raise IndexError("No se puede desencolar de una cola vacía")
        
        dato = self.frente_nodo.dato
        self.frente_nodo = self.frente_nodo.siguiente
        self._tamaño -= 1
        
        if self.esta_vacia():
            self.final_nodo = None
        
        return dato
    
    def frente(self):
        """Retorna el primer elemento sin removerlo"""
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.frente_nodo.dato
    
    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return self.frente_nodo is None
    
    def tamaño(self):
        """Retorna el número de elementos"""
        return self._tamaño
    
    def __str__(self):
        """Representación en string"""
        elementos = []
        nodo_actual = self.frente_nodo
        
        while nodo_actual:
            elementos.append(str(nodo_actual.dato))
            nodo_actual = nodo_actual.siguiente
        
        return f"ColaEnlazada: [{' -> '.join(elementos)}]"
    
    def mostrar_elementos(self):
        """Muestra todos los elementos de la cola"""
        elementos = []
        nodo_actual = self.frente_nodo
        
        while nodo_actual:
            elementos.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        
        return elementos


# Pruebas de la cola enlazada
if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBAS DE COLA ENLAZADA")
    print("=" * 60)
    print()
    
    cola = ColaEnlazada()
    
    # Prueba 1: Encolar elementos
    print("1. ENCOLANDO ELEMENTOS")
    print("-" * 60)
    for i in range(1, 6):
        cola.encolar(f"Cliente {i}")
        print(f"✓ Encolado Cliente {i}")
    
    print(f"Estado: {cola}")
    print(f"Tamaño: {cola.tamaño()}")
    print()
    
    # Prueba 2: Ver frente
    print("2. FRENTE DE LA COLA")
    print("-" * 60)
    print(f"Frente: {cola.frente()}")
    print()
    
    # Prueba 3: Desencolar
    print("3. DESENCOLANDO ELEMENTOS")
    print("-" * 60)
    while not cola.esta_vacia():
        cliente = cola.desencolar()
        print(f"✓ Atendiendo a: {cliente}")
        print(f"  Pendientes: {cola.tamaño()}")
    
    print()
    print("✅ Cola completamente vacía")

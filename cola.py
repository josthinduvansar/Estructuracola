"""
Implementación de una Cola (Queue) - FIFO (First In First Out)
Una cola es una estructura de datos donde el primer elemento en entrar
es el primero en salir.
"""

class Cola:
    """
    Clase que implementa una Cola usando una lista.
    Operaciones principales:
    - encolar (enqueue): agregar elemento al final
    - desencolar (dequeue): sacar elemento del principio
    - frente: obtener el elemento del frente sin remover
    - esta_vacia: verificar si la cola está vacía
    - tamaño: obtener la cantidad de elementos
    """
    
    def __init__(self):
        """Inicializa una cola vacía"""
        self.elementos = []
    
    def encolar(self, elemento):
        """
        Agrega un elemento al final de la cola
        Args:
            elemento: El valor a agregar
        """
        self.elementos.append(elemento)
    
    def desencolar(self):
        """
        Remueve y retorna el primer elemento de la cola
        Returns:
            El primer elemento de la cola
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("No se puede desencolar de una cola vacía")
        return self.elementos.pop(0)
    
    def frente(self):
        """
        Retorna el primer elemento sin removerlo
        Returns:
            El primer elemento de la cola
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.elementos[0]
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía
        Returns:
            True si está vacía, False en caso contrario
        """
        return len(self.elementos) == 0
    
    def tamaño(self):
        """
        Retorna la cantidad de elementos en la cola
        Returns:
            Número de elementos
        """
        return len(self.elementos)
    
    def __str__(self):
        """Representación en string de la cola"""
        return f"Cola: {self.elementos}"
    
    def __repr__(self):
        """Representación en string de la cola"""
        return f"Cola({self.elementos})"

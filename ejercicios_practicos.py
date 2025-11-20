"""
EJERCICIOS PRÁCTICOS ADICIONALES DE COLAS
Diversos ejercicios para reforzar el conocimiento de colas
"""

from cola import Cola


def ejercicio_1_inversión():
    """
    EJERCICIO 1: Invertir el orden de una cola usando una pila
    Usando operaciones básicas, invierte el orden de los elementos
    """
    print("=" * 60)
    print("EJERCICIO 1: INVERTIR EL ORDEN DE UNA COLA")
    print("=" * 60)
    print()
    
    # Crear cola original
    cola_original = Cola()
    elementos = [1, 2, 3, 4, 5]
    
    for elem in elementos:
        cola_original.encolar(elem)
    
    print(f"Cola original: {cola_original.elementos}")
    
    # Invertir usando una lista temporal (pila)
    pila_temporal = []
    while not cola_original.esta_vacia():
        pila_temporal.append(cola_original.desencolar())
    
    cola_invertida = Cola()
    while pila_temporal:
        cola_invertida.encolar(pila_temporal.pop())
    
    print(f"Cola invertida: {cola_invertida.elementos}")
    print()


def ejercicio_2_duplicar():
    """
    EJERCICIO 2: Duplicar todos los elementos de una cola
    """
    print("=" * 60)
    print("EJERCICIO 2: DUPLICAR ELEMENTOS DE UNA COLA")
    print("=" * 60)
    print()
    
    cola_original = Cola()
    elementos = [10, 20, 30, 40]
    
    for elem in elementos:
        cola_original.encolar(elem)
    
    print(f"Cola original: {cola_original.elementos}")
    
    cola_duplicada = Cola()
    
    # Guardar elementos mientras desencolamos
    temp = []
    while not cola_original.esta_vacia():
        elem = cola_original.desencolar()
        temp.append(elem)
        cola_duplicada.encolar(elem * 2)
    
    # Restaurar cola original
    for elem in temp:
        cola_original.encolar(elem)
    
    print(f"Cola original restaurada: {cola_original.elementos}")
    print(f"Cola duplicada: {cola_duplicada.elementos}")
    print()


def ejercicio_3_buscar():
    """
    EJERCICIO 3: Buscar un elemento en la cola
    Retorna la posición del elemento o -1 si no existe
    """
    print("=" * 60)
    print("EJERCICIO 3: BUSCAR ELEMENTO EN UNA COLA")
    print("=" * 60)
    print()
    
    def buscar_en_cola(cola, valor):
        """Busca un valor en la cola (sin modificarla)"""
        temp = Cola()
        posicion = -1
        contador = 0
        encontrado = False
        
        while not cola.esta_vacia():
            elem = cola.desencolar()
            if elem == valor and not encontrado:
                posicion = contador
                encontrado = True
            temp.encolar(elem)
            contador += 1
        
        # Restaurar la cola
        while not temp.esta_vacia():
            cola.encolar(temp.desencolar())
        
        return posicion
    
    cola = Cola()
    elementos = ["A", "B", "C", "D", "E"]
    for elem in elementos:
        cola.encolar(elem)
    
    print(f"Cola: {cola.elementos}")
    
    valor_buscado = "C"
    posicion = buscar_en_cola(cola, valor_buscado)
    
    if posicion != -1:
        print(f"✓ '{valor_buscado}' encontrado en posición {posicion}")
    else:
        print(f"✗ '{valor_buscado}' no encontrado en la cola")
    
    print()


def ejercicio_4_contar():
    """
    EJERCICIO 4: Contar elementos que cumplen una condición
    Cuenta cuántos elementos son mayores que un valor dado
    """
    print("=" * 60)
    print("EJERCICIO 4: CONTAR ELEMENTOS CON CONDICIÓN")
    print("=" * 60)
    print()
    
    def contar_mayores(cola, limite):
        """Cuenta elementos mayores que 'limite'"""
        temp = Cola()
        contador = 0
        
        while not cola.esta_vacia():
            elem = cola.desencolar()
            if elem > limite:
                contador += 1
            temp.encolar(elem)
        
        # Restaurar la cola
        while not temp.esta_vacia():
            cola.encolar(temp.desencolar())
        
        return contador
    
    cola = Cola()
    numeros = [5, 15, 8, 20, 3, 25, 10]
    for num in numeros:
        cola.encolar(num)
    
    print(f"Cola: {cola.elementos}")
    
    limite = 10
    cantidad = contar_mayores(cola, limite)
    print(f"Elementos mayores que {limite}: {cantidad}")
    print()


def ejercicio_5_filtrar():
    """
    EJERCICIO 5: Filtrar elementos de una cola
    Crea una nueva cola solo con los elementos pares
    """
    print("=" * 60)
    print("EJERCICIO 5: FILTRAR ELEMENTOS PARES DE UNA COLA")
    print("=" * 60)
    print()
    
    cola_original = Cola()
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for num in numeros:
        cola_original.encolar(num)
    
    print(f"Cola original: {cola_original.elementos}")
    
    # Filtrar pares
    cola_pares = Cola()
    temp = Cola()
    
    while not cola_original.esta_vacia():
        elem = cola_original.desencolar()
        temp.encolar(elem)
        if elem % 2 == 0:
            cola_pares.encolar(elem)
    
    # Restaurar original
    while not temp.esta_vacia():
        cola_original.encolar(temp.desencolar())
    
    print(f"Cola filtrada (pares): {cola_pares.elementos}")
    print()


def ejercicio_6_sumar():
    """
    EJERCICIO 6: Sumar todos los elementos de una cola
    """
    print("=" * 60)
    print("EJERCICIO 6: SUMA DE ELEMENTOS DE UNA COLA")
    print("=" * 60)
    print()
    
    def sumar_elementos(cola):
        """Suma todos los elementos de la cola"""
        temp = Cola()
        suma = 0
        
        while not cola.esta_vacia():
            elem = cola.desencolar()
            suma += elem
            temp.encolar(elem)
        
        # Restaurar la cola
        while not temp.esta_vacia():
            cola.encolar(temp.desencolar())
        
        return suma
    
    cola = Cola()
    numeros = [10, 20, 30, 40, 50]
    for num in numeros:
        cola.encolar(num)
    
    print(f"Cola: {cola.elementos}")
    
    total = sumar_elementos(cola)
    print(f"Suma total: {total}")
    print()


def ejercicio_7_mezclar():
    """
    EJERCICIO 7: Mezclar dos colas en una sola
    Intercala elementos de dos colas
    """
    print("=" * 60)
    print("EJERCICIO 7: MEZCLAR DOS COLAS")
    print("=" * 60)
    print()
    
    cola1 = Cola()
    cola2 = Cola()
    
    for num in [1, 3, 5]:
        cola1.encolar(num)
    
    for num in [2, 4, 6]:
        cola2.encolar(num)
    
    print(f"Cola 1: {cola1.elementos}")
    print(f"Cola 2: {cola2.elementos}")
    
    cola_mezcla = Cola()
    
    # Mezclar intercalando
    while not cola1.esta_vacia() or not cola2.esta_vacia():
        if not cola1.esta_vacia():
            cola_mezcla.encolar(cola1.desencolar())
        if not cola2.esta_vacia():
            cola_mezcla.encolar(cola2.desencolar())
    
    print(f"Cola mezclada: {cola_mezcla.elementos}")
    print()


def ejercicio_8_rotacion():
    """
    EJERCICIO 8: Rotar elementos de una cola
    Mueve los primeros n elementos al final
    """
    print("=" * 60)
    print("EJERCICIO 8: ROTACIÓN DE COLA")
    print("=" * 60)
    print()
    
    def rotar_cola(cola, n):
        """Rota n elementos hacia el final"""
        if cola.esta_vacia():
            return
        
        # Rotar n veces
        for _ in range(n):
            elemento = cola.desencolar()
            cola.encolar(elemento)
    
    cola = Cola()
    elementos = [1, 2, 3, 4, 5]
    for elem in elementos:
        cola.encolar(elem)
    
    print(f"Cola original: {cola.elementos}")
    
    rotar_cola(cola, 2)
    print(f"Cola después de rotar 2 posiciones: {cola.elementos}")
    print()


if __name__ == "__main__":
    ejercicio_1_inversión()
    ejercicio_2_duplicar()
    ejercicio_3_buscar()
    ejercicio_4_contar()
    ejercicio_5_filtrar()
    ejercicio_6_sumar()
    ejercicio_7_mezclar()
    ejercicio_8_rotacion()

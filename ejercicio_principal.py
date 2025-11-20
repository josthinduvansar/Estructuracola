"""
EJERCICIO PRINCIPAL: Simulación de una Cola de Atención al Cliente
En este ejercicio simularemos una fila de espera en un banco o tienda.
"""

from cola import Cola
from datetime import datetime

def ejercicio_cola_atencion():
    """
    Simula una cola de atención al cliente en un banco
    """
    print("=" * 60)
    print("SISTEMA DE COLA DE ATENCIÓN AL CLIENTE")
    print("=" * 60)
    print()
    
    # Crear una cola para los clientes
    cola_clientes = Cola()
    
    # Simular llegada de clientes
    clientes = ["Juan García", "María López", "Carlos Rodríguez", 
                "Ana Martínez", "Pedro Sánchez"]
    
    print("📋 LLEGADA DE CLIENTES A LA COLA")
    print("-" * 60)
    for cliente in clientes:
        cola_clientes.encolar(cliente)
        print(f"✓ {cliente} llegó y se encoló")
        print(f"  Clientes en la cola: {cola_clientes.tamaño()}")
    
    print()
    print("=" * 60)
    print("📊 ESTADO ACTUAL DE LA COLA")
    print("-" * 60)
    print(f"Frente de la cola: {cola_clientes.frente()}")
    print(f"Total de clientes esperando: {cola_clientes.tamaño()}")
    print(f"Estado: {cola_clientes}")
    
    print()
    print("=" * 60)
    print("🏦 ATENCIÓN DE CLIENTES")
    print("-" * 60)
    
    contador_atendidos = 1
    while not cola_clientes.esta_vacia():
        cliente = cola_clientes.desencolar()
        print(f"🔔 Atendiendo al cliente #{contador_atendidos}: {cliente}")
        print(f"   Clientes pendientes: {cola_clientes.tamaño()}")
        contador_atendidos += 1
    
    print()
    print("=" * 60)
    print("✅ TODOS LOS CLIENTES HAN SIDO ATENDIDOS")
    print("=" * 60)


def ejercicio_procesar_tareas():
    """
    Simula el procesamiento de tareas en una cola de trabajo
    """
    print("\n\n")
    print("=" * 60)
    print("EJERCICIO 2: COLA DE PROCESAMIENTO DE TAREAS")
    print("=" * 60)
    print()
    
    cola_tareas = Cola()
    
    tareas = [
        {"id": 1, "descripcion": "Generar reporte", "prioridad": "Alta"},
        {"id": 2, "descripcion": "Actualizar base de datos", "prioridad": "Media"},
        {"id": 3, "descripcion": "Enviar email", "prioridad": "Baja"},
        {"id": 4, "descripcion": "Respaldar archivos", "prioridad": "Alta"},
        {"id": 5, "descripcion": "Limpiar caché", "prioridad": "Baja"},
    ]
    
    print("📝 TAREAS ENCOLADAS")
    print("-" * 60)
    for tarea in tareas:
        cola_tareas.encolar(tarea)
        print(f"✓ Tarea {tarea['id']}: {tarea['descripcion']} ({tarea['prioridad']})")
    
    print()
    print("=" * 60)
    print("⚙️  PROCESAMIENTO DE TAREAS")
    print("-" * 60)
    
    tiempo_actual = 1
    while not cola_tareas.esta_vacia():
        tarea = cola_tareas.desencolar()
        print(f"\n[Tiempo: {tiempo_actual}s] Procesando tarea {tarea['id']}")
        print(f"  Descripción: {tarea['descripcion']}")
        print(f"  Prioridad: {tarea['prioridad']}")
        print(f"  Tareas pendientes: {cola_tareas.tamaño()}")
        tiempo_actual += 2


def ejercicio_operaciones_basicas():
    """
    Ejercicio para practicar operaciones básicas de una cola
    """
    print("\n\n")
    print("=" * 60)
    print("EJERCICIO 3: OPERACIONES BÁSICAS DE COLA")
    print("=" * 60)
    print()
    
    cola = Cola()
    
    # Operación 1: Encolar elementos
    print("1️⃣  ENCOLANDO ELEMENTOS")
    print("-" * 60)
    numeros = [10, 20, 30, 40, 50]
    for num in numeros:
        cola.encolar(num)
        print(f"Encolado: {num} | Cola actual: {cola.elementos}")
    
    print()
    
    # Operación 2: Consultar frente
    print("2️⃣  CONSULTANDO EL FRENTE")
    print("-" * 60)
    print(f"Frente actual: {cola.frente()}")
    
    print()
    
    # Operación 3: Desencolar elementos
    print("3️⃣  DESENCOLANDO ELEMENTOS")
    print("-" * 60)
    while not cola.esta_vacia():
        elemento = cola.desencolar()
        print(f"Desencolado: {elemento} | Cola restante: {cola.elementos}")
    
    print()
    
    # Operación 4: Intento de desencolar cola vacía
    print("4️⃣  MANEJO DE ERRORES")
    print("-" * 60)
    if cola.esta_vacia():
        print("✓ La cola está vacía")
        try:
            cola.desencolar()
        except IndexError as e:
            print(f"❌ Error capturado: {e}")


def menu_interactivo():
    """
    Menú interactivo para practicar con la cola
    """
    print("\n\n")
    print("=" * 60)
    print("EJERCICIO 4: SIMULADOR INTERACTIVO DE COLA")
    print("=" * 60)
    print()
    
    cola = Cola()
    
    while True:
        print("\n📌 OPCIONES:")
        print("1. Encolar un elemento")
        print("2. Desencolar un elemento")
        print("3. Ver frente de la cola")
        print("4. Ver tamaño de la cola")
        print("5. Ver toda la cola")
        print("6. ¿La cola está vacía?")
        print("7. Salir")
        print()
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            elemento = input("Ingrese el elemento a encolar: ").strip()
            cola.encolar(elemento)
            print(f"✓ '{elemento}' ha sido encolado")
        
        elif opcion == "2":
            if cola.esta_vacia():
                print("❌ La cola está vacía, no hay nada que desencolar")
            else:
                elemento = cola.desencolar()
                print(f"✓ '{elemento}' ha sido desencolado")
        
        elif opcion == "3":
            if cola.esta_vacia():
                print("❌ La cola está vacía")
            else:
                print(f"📍 Frente de la cola: {cola.frente()}")
        
        elif opcion == "4":
            print(f"📊 Tamaño de la cola: {cola.tamaño()}")
        
        elif opcion == "5":
            print(f"📋 Cola completa: {cola}")
        
        elif opcion == "6":
            if cola.esta_vacia():
                print("✓ Sí, la cola está vacía")
            else:
                print("✗ No, la cola NO está vacía")
        
        elif opcion == "7":
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    # Ejecutar ejercicios automáticos
    ejercicio_cola_atencion()
    ejercicio_procesar_tareas()
    ejercicio_operaciones_basicas()
    
    # Descomentar la siguiente línea para usar el menú interactivo
    # menu_interactivo()

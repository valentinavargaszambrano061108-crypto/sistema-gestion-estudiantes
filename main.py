# ======================================
# SISTEMA DE GESTIÓN DE ESTUDIANTES
# ======================================

# Lista donde se almacenan los estudiantes
lista_estudiantes = []

# Variable de conteo
contador_estudiantes = 0

# Bandera para controlar salida
bandera_salir = False


# --------------------------------------
# FUNCIÓN AGREGAR ESTUDIANTE
# --------------------------------------
def agregar_estudiante():

    global contador_estudiantes

    print("\n--- AGREGAR ESTUDIANTE ---")

    try:
        id_estudiante = int(input("Ingrese ID: "))
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))

        # Validar ID repetido
        for estudiante in lista_estudiantes:
            if estudiante["id"] == id_estudiante:
                print("Ese ID ya existe.")
                return

        estudiante = {
            "id": id_estudiante,
            "nombre": nombre,
            "edad": edad
        }

        lista_estudiantes.append(estudiante)

        contador_estudiantes += 1

        print("Estudiante agregado correctamente.")

    except ValueError:
        print("Error: Ingrese datos válidos.")


# --------------------------------------
# FUNCIÓN MOSTRAR ESTUDIANTES
# --------------------------------------
def mostrar_estudiantes():

    print("\n--- LISTA DE ESTUDIANTES ---")

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")

    else:
        for estudiante in lista_estudiantes:

            print("---------------------")
            print("ID:", estudiante["id"])
            print("Nombre:", estudiante["nombre"])
            print("Edad:", estudiante["edad"])


# --------------------------------------
# FUNCIÓN BUSCAR ESTUDIANTE
# --------------------------------------
def buscar_estudiante():

    print("\n--- BUSCAR ESTUDIANTE ---")

    try:
        id_busqueda = int(input("Ingrese ID a buscar: "))

        encontrado = False

        for estudiante in lista_estudiantes:

            if estudiante["id"] == id_busqueda:

                print("\nEstudiante encontrado")
                print("ID:", estudiante["id"])
                print("Nombre:", estudiante["nombre"])
                print("Edad:", estudiante["edad"])

                encontrado = True
                break

        if not encontrado:
            print("No se encontró el estudiante.")

    except ValueError:
        print("Debe ingresar números válidos.")


# --------------------------------------
# MENÚ PRINCIPAL
# --------------------------------------
while not bandera_salir:

    print("""
===================================
 SISTEMA DE GESTIÓN ESTUDIANTIL
===================================
1. Agregar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Salir
===================================
""")

    opcion = input("Seleccione una opción: ")

    # Estructuras de decisión
    if opcion == "1":
        agregar_estudiante()

    elif opcion == "2":
        mostrar_estudiantes()

    elif opcion == "3":
        buscar_estudiante()

    elif opcion == "4":

        print("Saliendo del sistema...")
        bandera_salir = True

    else:
        print("Opción inválida.")


print("\nPrograma finalizado.")
print("Total estudiantes:", contador_estudiantes)

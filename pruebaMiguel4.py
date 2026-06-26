

def mostrarMen():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")


def leerop():
    while True:
        try:
            opcion = int(input("Ingrese opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: la opción debe ser un número entre 1 y 6.")
        except ValueError:
            print("Error: ingrese un número válido.")


def validarTt(titulo):
    if titulo.strip() == "":
        return False
    return True


def validarD(duracion):
    try:
        duracion = int(duracion)
        if duracion > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def validarC(calificacion):
    try:
        calificacion = float(calificacion)
        if 0.0 <= calificacion <= 10.0:
            return True
        else:
            return False
    except ValueError:
        return False


def agregarPL(pli):
    print("\n--- AGREGAR PELÍCULA ---")

    titulo = input("Ingrese el título: ")
    if not validarTt(titulo):
        print("Error: el título no puede estar vacío.")
        return

    duracion = input("Ingrese la duración en minutos: ")
    if not validarD(duracion):
        print("Error: la duración debe ser un entero mayor que 0.")
        return

    calificacion = input("Ingrese la calificación (0.0 - 10.0): ")
    if not validarC(calificacion):
        print("Error: la calificación debe estar entre 0.0 y 10.0.")
        return

    pelicula = {
        "titulo": titulo.strip(),
        "duracion": int(duracion),
        "calificacion": float(calificacion),
        "disponible": False
    }

    pli.append(pelicula)

    print(f"Película '{titulo}' agregada correctamente.")


def buscar_pel(pli, titulo_buscar):
    for i in range(len(pli)):
        if pli[i]["titulo"].lower() == titulo_buscar.lower():
            return i
    return -1


def mostrar_d_peli(pelicula, posicion):
    print(f"\nPelícula encontrada en posición {posicion}")
    print(f"Título: {pelicula['titulo']}")
    print(f"Duración: {pelicula['duracion']}")
    print(f"Calificación: {pelicula['calificacion']}")

    estado = "DISPONIBLE" if pelicula["disponible"] else "NO RECOMENDADA"
    print(f"Estado: {estado}")


def eliminar_pelicula(pli, titulo_eliminar):
    posicion = buscar_pel(pli, titulo_eliminar)

    if posicion != -1:
        pli.pop(posicion)
        print(f"Película '{titulo_eliminar}' eliminada correctamente.")
    else:
        print(f"La película '{titulo_eliminar}' no se encuentra registrada.")


def actualizarDispo(pli):
    for pelicula in pli:
        if pelicula["calificacion"] >= 7.0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

    print("Disponibilidad actualizada correctamente.")


def mostrar_pelicula(pli):

    actualizarDispo(pli)

    if len(pli) == 0:
        print("No hay películas registradas.")
        return

    print("\n=== LISTA DE PELÍCULAS ===")

    for pelicula in pli:
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificacion']}")

        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")

        print("*" * 40)



peliculas = []

while True:

    mostrarMen()
    opcion = leerop()

    if opcion == 1:
        agregarPL(peliculas)

    elif opcion == 2:
        titulo = input("Ingrese el título a buscar: ")

        posicion = buscar_pel(peliculas, titulo)

        if posicion != -1:
            mostrar_d_peli(peliculas[posicion], posicion)
        else:
            print("Película no encontrada.")

    elif opcion == 3:
        titulo = input("Ingrese el título de la película a eliminar: ")
        eliminar_pelicula(peliculas, titulo)

    elif opcion == 4:
        actualizarDispo(peliculas)

    elif opcion == 5:
        mostrar_pelicula(peliculas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break
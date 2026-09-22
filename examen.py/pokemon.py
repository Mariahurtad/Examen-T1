import random

def crearEntrenador(tupla):

    nombreEntrenador = input("Ingrese nombre del entrenador: ")
    nombrePokemon = input("Ingrese nombre del Pokemon: ")

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)

    pokemon = (nombreEntrenador, nombrePokemon, ataque, vida)

    tupla.append(pokemon)

    print("Entrenador creado correctamente.")


def listaEntrenador(tupla):

    for i in range(1, len(tupla)):

        for j in range(len(tupla) - 1):

            if tupla[j][2] > tupla[j + 1][2]:

                tupla[j], tupla[j + 1] = tupla[j + 1], tupla[j]

    print("\nLISTA DE POKEMONES")

    for i in range(len(tupla)):

        print(
            f"{i + 1}. "
            f"Entrenador: {tupla[i][0]} | "
            f"Pokemon: {tupla[i][1]} | "
            f"Ataque: {tupla[i][2]} | "
            f"Vida: {tupla[i][3]}"
        )


def borraPorPokemon(tupla):

    if len(tupla) == 0:
        print("No hay Pokemones registrados.")
        return

    vidaBuscada = int(input("Ingrese la vida a buscar: "))


    for i in range(len(tupla)):
        ind_min_val = i

        for j in range(i + 1, len(tupla)):
            if tupla[j][3] < tupla[ind_min_val][3]:
                ind_min_val = j

        if ind_min_val != i:
            tupla[i], tupla[ind_min_val] = tupla[ind_min_val], tupla[i]

    izquierda = 0
    derecha = len(tupla) - 1
    posicion = -1

    # Búsqueda binaria para encontrar la primera coincidencia de vida
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if tupla[medio][3] == vidaBuscada:
            posicion = medio
            derecha = medio - 1
        elif tupla[medio][3] < vidaBuscada:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    if posicion == -1:
        print("No se encontro un Pokemon con esa vida.")
        return

    eliminado = tupla.pop(posicion)

    print(
        f"Se elimino a {eliminado[0]} "
        f"con su Pokemon {eliminado[1]}."
    )


def peleaPokemon(lista):

    if len(lista) < 2:
        print("No hay suficientes Pokemones para pelear.")
        return

    listaEntrenador(lista)

    pokemon1 = int(input("Ingrese el numero del primer Pokemon: "))
    pokemon2 = int(input("Ingrese el numero del segundo Pokemon: "))

    pokemon1 = pokemon1 - 1
    pokemon2 = pokemon2 - 1

    if pokemon1 == pokemon2:
        print("Debe seleccionar dos Pokemones diferentes.")
        return

    multiplicador1 = random.randint(0, 5)
    multiplicador2 = random.randint(0, 5)

    danio1 = lista[pokemon1][2] * multiplicador1
    danio2 = lista[pokemon2][2] * multiplicador2

    vida1 = lista[pokemon1][3] - danio2
    vida2 = lista[pokemon2][3] - danio1

    print("\n--- PELEA ---")

    print(
        f"{lista[pokemon1][1]} atacó con "
        f"{lista[pokemon1][2]} x {multiplicador1}"
    )

    print(
        f"{lista[pokemon2][1]} atacó con "
        f"{lista[pokemon2][2]} x {multiplicador2}"
    )

    if vida1 <= 0 and vida2 <= 0:

        print("Ambos Pokemones perdieron.")

        lista.pop(max(pokemon1, pokemon2))
        lista.pop(min(pokemon1, pokemon2))

    elif vida1 > vida2:

        print(
            f"Ganó {lista[pokemon1][0]} "
            f"con su Pokemon {lista[pokemon1][1]}."
        )

        lista.pop(pokemon2)

    elif vida2 > vida1:

        print(
            f"Ganó {lista[pokemon2][0]} "
            f"con su Pokemon {lista[pokemon2][1]}."
        )

        lista.pop(pokemon1)

    else:

        print("Empataron. Ambos Pokemones pierden.")

        lista.pop(max(pokemon1, pokemon2))
        lista.pop(min(pokemon1, pokemon2))




tupla = []

while True:

    print("\n========== MENU ==========")
    print("1. Crear Entrenador")
    print("2. Listar Entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelea Pokemon")
    print("5. Fin")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:

        crearEntrenador(tupla)

    elif opcion == 2:

        listaEntrenador(tupla)

    elif opcion == 3:

        borraPorPokemon(tupla)

    elif opcion == 4:

        peleaPokemon(tupla)

    elif opcion == 5:

        print("Fin del programa.")
        break

    else:

        print("Opción inválida.")
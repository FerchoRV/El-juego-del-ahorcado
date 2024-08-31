# main.py

from utils import seleccionar_palabra,obtener_letra, actualizar_juego, mostrar_progreso


def jugar():
    """Función principal que maneja la lógica del juego del ahorcado."""
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    letras_erroneas = set()
    intentos = 0
    max_intentos = 6  # Este valor puede estar basado en el largo de `ahorcado` en arte.py

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos < max_intentos:
        mostrar_progreso(intentos, letras_adivinadas, letras_erroneas, palabra)

        letra = obtener_letra()

        if letra in letras_adivinadas or letra in letras_erroneas:
            print("Ya has adivinado esa letra, intenta con otra.")
            continue

        if not actualizar_juego(letra, palabra, letras_adivinadas, letras_erroneas):
            intentos += 1

        if set(palabra) == letras_adivinadas:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break

    if intentos == max_intentos:
        mostrar_progreso(intentos, letras_adivinadas, letras_erroneas, palabra)
        print(f"Lo siento, has sido ahorcado. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()

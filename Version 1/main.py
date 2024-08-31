# main.py

import random
from palabras import palabras
from arte import ahorcado

def seleccionar_palabra():
    """Selecciona aleatoriamente una palabra de la lista de palabras."""
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    """Muestra el estado actual de la palabra adivinada."""
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def jugar():
    """Función principal que contiene la lógica del juego del ahorcado."""
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    letras_erroneas = set()
    intentos = 0
    max_intentos = len(ahorcado) - 1

    print("¡Bienvenido al juego del Ahorcado!")

    while intentos < max_intentos:
        print(ahorcado[intentos])
        print("Palabra:", mostrar_estado(palabra, letras_adivinadas))
        print("Letras adivinadas:", ' '.join(sorted(letras_adivinadas)))
        print("Letras incorrectas:", ' '.join(sorted(letras_erroneas)))

        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if letra in letras_adivinadas or letra in letras_erroneas:
            print("Ya has adivinado esa letra, intenta con otra.")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            if set(palabra) == letras_adivinadas:
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            letras_erroneas.add(letra)
            intentos += 1

    if intentos == max_intentos:
        print(ahorcado[intentos])
        print(f"Lo siento, has sido ahorcado. La palabra era: {palabra}")

if __name__ == "__main__":
    jugar()

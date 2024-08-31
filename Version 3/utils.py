# utils.py

import random
from palabras import palabras
from arte import ahorcado

def seleccionar_palabra():
    """Selecciona aleatoriamente una palabra de la lista de palabras."""
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    """Muestra el estado actual de la palabra adivinada."""
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def obtener_letra():
    """Solicita al usuario que ingrese una letra válida."""
    while True:
        letra = input("Adivina una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        print("Por favor, ingresa una letra válida.")

def actualizar_juego(letra, palabra, letras_adivinadas, letras_erroneas):
    """Actualiza las letras adivinadas o las letras erróneas según la letra ingresada."""
    if letra in palabra:
        letras_adivinadas.add(letra)
        return True
    else:
        letras_erroneas.add(letra)
        return False

def mostrar_progreso(intentos, letras_adivinadas, letras_erroneas, palabra):
    """Muestra el progreso del juego: dibujo del ahorcado, estado de la palabra, letras adivinadas y letras incorrectas."""
    print(ahorcado[intentos])
    print("Palabra:", mostrar_estado(palabra, letras_adivinadas))
    print("Letras adivinadas:", ' '.join(sorted(letras_adivinadas)))
    print("Letras incorrectas:", ' '.join(sorted(letras_erroneas)))

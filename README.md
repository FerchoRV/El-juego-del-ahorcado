## Ejercitación El juego del ahorcado

El juego del ahorcado es simple, el jugador debe adivinar una
palabra, seleccionada aleatoriamente de una lista de
palabras, el usuario verá espacios vacíos (guiones bajos) que
representan la cantidad de caracteres de la palabra. Para
adivinar la palabra el usuario debe indicar una letra a la vez, si
la letra se incluye en la palabra, deberá reemplazar el espacio
vacío por la letra correspondiente, tantas como contenga la
palabra, en caso de la letra no encontrarse en la palabra, se
deberá presentar un muñeco al que se le irán pintando sus
extremidades hasta completarlo, una extremidad por cada
error del usuario.
El juego termina cuando el jugador completa la palabra antes
de ser ahorcado y se dará como ganador o cuando el muñeco
del usuario sea dibujado completamente y se dará como
perdedor.
El proyecto se desarrollará en 3 archivos, el archivo main que
contiene toda la lógica del juego, el archivo de palabras, que
contiene una lista con todas las palabras con las que se va a
jugar y el archivo del arte, que contendra una lista con los
dibujos del ahorcado en cada una de sus etapas.

## Soluciones 

**1- Versión 1** 

Archivos separados como lo pide el texto

**2- Versión 2** 

Archivos separados pero el documento main se encuentra modularizado es decir más funciones que la versión 1

**3- Versión 3**

Es la versión donde se encapsula todas las herramientas en un solo documentos y este se importa en el main para mostrar la importación de múltiples funciones propias de un documento.

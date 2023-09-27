
## Ejercicio 6:

import random

puntos = 0
veces = 0

adivinanzas = {
    1: "¿Qué cosa es que cuanto más le quitas más grande es?\na. Un agujero, b. Un coche, c. Un río: ",
    2: "No muerde ni ladra, pero tiene dientes y la casa guarda. ¿Qué es?\na. Una llave, b. Un gato, c. Una puerta: ",
    3: "Adivina, esta difícil adivinanza, ¿cuál es el ave que tiene la panza llana?\na. Una avellana, b. Una cigüeña, c. Un avión de papel: ",
}

claves_adivinanzas = list(adivinanzas.keys())

while veces < 3:
    sel = random.sample(claves_adivinanzas, 1)[0]
    claves_adivinanzas.remove(sel) 

    print(adivinanzas[sel])
    sol = input("\t")
    veces += 1

    if sel == 1:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5
    elif sel == 2:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5
    elif sel == 3:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5

print("Ha finalizado el juego. Felicidades, tienes un total de: " + str(puntos) + "\n")

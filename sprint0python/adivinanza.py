## Ejercicio 1:

print("")
print("¿Qué cosa es que cuanto más le quitas más grande es? ")
sol = input ("a. Un agujero, b. Un coche, c. Un río: ")
print("")

puntos=0

if(sol != 'a'):
    print("Error. Esa es la respuesta incorrecta.\n")
    puntos=puntos-5
else:
    print("¡Enhorabuena! Has acertado.\n")
    puntos=puntos+10

## Ejercicio 2:


print("No muerde ni ladra, pero tiene dientes y la casa guarda. ¿Qué es?")
sol = input ("a. Una llave, b. Un gato, c. Una puerta: ")
print("")

if(sol != 'a'):
    print("Error. Esa es la respuesta incorrecta.\n")
    puntos=puntos-5
else:
    print("¡Enhorabuena! Has acertado.\n")
    puntos=puntos+10


print("Adivina, esta difícil adivinanza, ¿cuál es el ave que tiene la panza llana?")
sol = input ("a. Una avellana, b. Una cigueña, c. Un avión de papel: ")

if(sol != 'a'):
    print("Error. Esa es la respuesta incorrecta.\n")
    puntos=puntos-5
else:
    print("¡Enhorabuena! Has acertado.\n")
    puntos=puntos+10

print("Ha finalizado el juego. Felicidades, tienes un total de: "+str(puntos))
print("\n")
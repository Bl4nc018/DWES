import random

## Ejercicio 5:

print("Iniciando el siguiente juego: 'Piedra, papel y tijera.'")

pMaquina=0
pJugador=0
veces=0

while veces<=5:
    jugador=int(input("\nSeleccione lo que va a jugar. 1. Piedra, 2. Papel o 3. Tijera: "))

    maquina = random.randint(1,3)

    if jugador==maquina :
        print("¡Empate! Vuelva a intentarlo. Esta jugada no será contada.")
    elif jugador==1 and maquina==2: 
        print("Se siente. Ganó la máquina. \n Papel le gana a piedra.")
        pMaquina=pMaquina+1
        veces=veces+1
    elif jugador==2 and maquina==3:
        print("Se siente. Ganó la máquina. \n Tijera le gana a papel.")
        pMaquina=pMaquina+1
        veces=veces+1
    elif jugador==3 and maquina==1:
        print("Se siente. Ganó la máquina. \n Piedra le gana a tijera.")
        pMaquina=pMaquina+1
        veces=veces+1
    elif jugador==2 and maquina==1:
        print("¡Enhorabuena! Ganaste.\n Papel le gana a piedra.")
        pJugador=pJugador+1
        veces=veces+1
    elif jugador==3 and maquina==2:
        print("¡Enhorabuena! Ganaste.\n Tijera le gana a papel.")
        pJugador=pJugador+1
        veces=veces+1
    elif jugador==1 and maquina==3:
        print("¡Enhorabuena! Ganaste.\n Piedra le gana a tijera.")
        pJugador=pJugador+1
        veces=veces+1

print("\nTu total de puntos es: "+str(pJugador)+". Y el total de puntos de la máquina es: "+str(pMaquina))
if pJugador>pMaquina:
    print ("¡Enhorabuena! Has ganado el juego.")
elif pJugador == pMaquina:
    print("Habeis empatado. ¡No pasa nada!")
else:  
    print ("¡Buen intento! Ya ganarás en la siguiente.")

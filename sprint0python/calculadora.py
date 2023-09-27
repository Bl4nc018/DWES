## Ejercicio 4:

from operaciones import suma, resta, multiplicacion, division

repetir = "s"

while repetir == 's':
    numero1 = int(input("\nIntroduzca el primer número: "))
    numero2 = int(input("Ahora, el segundo número:  "))

    operacion = input("\nIndique el tipo de operación que desee llevar a cabo: ")

    if operacion == 'suma':
        opSolucion=suma(numero1, numero2)
        print("\nEl resultado de su operación es: "+str(opSolucion))
    elif operacion == 'resta':
        opSolucion=resta(numero1, numero2)
        print("\nEl resultado de su operación es: "+str(opSolucion))
    elif operacion == 'multiplicacion':
        opSolucion=multiplicacion(numero1, numero2)
        print("\nEl resultado de su operación es: "+str(opSolucion))
    elif operacion == 'division':
        opSolucion=division(numero1, numero2)
        if numero1==0 or numero2==0:
            repetir = input("\n¿Desea utilizar de nuevo la calculadora? (s/n): ")
        print("\nEl resultado de su operación es: "+str(opSolucion))

    repetir = input("\n¿Desea utilizar de nuevo la calculadora? (s/n): ")

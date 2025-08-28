import os

isActive = True
while isActive:
    os.system("cls")
    print("Bienvenido al generador de triangulos")
    try:
        n = int(input("Ingrese la cantidad de la base del triangulo\nPresione 0 si desea salir\n"))
        if n == 0:
            isActive = False
            print("Gracias por usar el programa")
        elif n > 1:
            for i in range(1, n + 1):
                print("*" * i)
            os.system("pause")
        else:
            print("No existe un triangulo con base 1")
            os.system("pause")
    except ValueError:
        print("Debe ingresar un numero entero")
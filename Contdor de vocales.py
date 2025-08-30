import os

os.system("clear")
print("BIENVENIDO AL PROGRAMA CONTADOR DE VOCALES")
isActive = True
while isActive:
   
    frase = input("Escribe una palabra o frase para contar sus vocales: ").lower()

    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    

    for letra in frase:
        if letra == 'a':
            contador_a += 1            
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1            
        elif letra == 'u':
            contador_u += 1
        elif letra==0:
            break
        else:
            print("Su texto no contiene vocales")


    print("\n--- RESULTADO DEL CONTEO ---")
    print(f"La vocal 'a' aparece: {contador_a} veces")
    print(f"La vocal 'e' aparece: {contador_e} veces")
    print(f"La vocal 'i' aparece: {contador_i} veces")
    print(f"La vocal 'o' aparece: {contador_o} veces")
    print(f"La vocal 'u' aparece: {contador_u} veces")
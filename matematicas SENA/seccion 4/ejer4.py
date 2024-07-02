numero = int(input("Ingrese un número entre 1 y 15: "))
if 1 <= numero <= 15:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print("El número ingresado no está en el rango especificado.")

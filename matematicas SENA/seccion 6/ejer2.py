def suma_numero (n):
    suma =  n * (n + 1) //2
    return suma
numero=int(input("Ingrese un número : "))
resultado=suma_numero(numero)
print (f"la suma de los primeros número de { numero} es {resultado}")
def mostrar_numeros (n):
    if n <1:
        print ("ingresa un número positivo") 
    else:
     for i in range (1,n + 1):
        print (i)

numero=int(input("Ingrese un número : "))
mostrar_numeros(numero)
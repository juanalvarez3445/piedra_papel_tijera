"""
Aplcacion que prove una interfaz al usuario 
paa ejecutar operaciones basicas entre dos numeros 
Autor: Kevin Manuel 
fecha: 6 de octubre 2023
"""
# que operación quiere hacer el husuario 

opcion = input ("para sumar ingrese 1 para restar ingrese 2 para multiplicar ingrese 3 para dividir ingrese 4: " )

# pidamos los numero

numero1 = int (input("ingresa numero 1: "))
numero2 = int (input("ingresa numero 2: "))

# si la opcoón es 1 sumamos 

if opcion == "1": 
    operación = numero1 + numero2
    
    # si la opcoón es 1 sumamos 4

if opcion == "2": 
    operación = numero1 - numero2
    
    # si la opcoón es 1 sumamos 

if opcion == "3": 
    operación = numero1 * numero2
    
    # si la opcoón es 1 sumamos 

if opcion == "4": 
    operación = numero1 / numero2
    
print("resultado de la operación " + str (operación))
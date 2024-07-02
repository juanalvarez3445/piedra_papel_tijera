def calcular_promedio():
    numeros = []
    
    while True:
            
            numero = float(input("Ingrese un número (ingrese 0 para finalizar): "))
            if numero == 0:
                  break
            else:
                numeros.append(numero)

    if not numeros:
        print("No se ingresaron números.")
    else:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números ingresados es: {promedio}")

if __name__ == "__main__":
    calcular_promedio()

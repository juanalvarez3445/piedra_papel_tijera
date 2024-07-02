def suma_cuadrados(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i**2
    return suma

if __name__ == "__main__":
    entrada_valida = False

    while not entrada_valida:
        valor_n = input("Ingrese un valor entero para n: ")
        
        if valor_n.isdigit():
            n = int(valor_n)
            entrada_valida = True
        else:
            print(" ingrese un número entero válido.")

    resultado = suma_cuadrados(n)
    print(f"La suma de los cuadrados de los números entre 1 y {n} es: {resultado}")

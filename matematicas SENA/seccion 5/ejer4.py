def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))
    resultado_factorial = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado_factorial}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
def numeros_impares (n):
  for numero in range(1, n + 1, 2):
        print(numero)
numero = int(input("Ingrese un número para mostrar los números impares hasta este valor : "))
print(f"Números impares hasta {numero}:\n")
numeros_impares(numero)
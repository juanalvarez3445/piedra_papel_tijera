n1=int(input("Ingrese el primero número : "))
n2=int(input("Ingrese el segundo número: "))
n3=int(input("Ingrese el trecer número : "))
if n1 == n2 == n3:
    print(f"Los tres números son iguales. Valor: {n1}")
else:
    mayor = max(n1, n2, n3)
    print(f"El número mayor es: {mayor}")
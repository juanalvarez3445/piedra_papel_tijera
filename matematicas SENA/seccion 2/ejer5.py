"""juan carlos ceballos"""
# ingrese  precio del producto
precio_producto = float(input("Ingrese el precio del producto: "))

# Calcular el descuento del 10%
descuento = precio_producto * 0.10

# Calcular el precio final restando el descuento al precio original
precio_final = precio_producto - descuento

# Imprimir el precio final al consumidor
print(f"el valor del producto es: {precio_producto:.0f} El precio final con un descuento del 10% es: {precio_final:.2f}")
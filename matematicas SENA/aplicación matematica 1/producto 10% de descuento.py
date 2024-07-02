valor_producto = float(input("Ingresa el valor del producto: "))

descuento = valor_producto * 0.10

precio_con_descuento = valor_producto - descuento

print(f"El precio original del producto es: ${valor_producto}")
print(f"Descuento del 10%: ${descuento}")
print(f"Precio con descuento: ${precio_con_descuento}")
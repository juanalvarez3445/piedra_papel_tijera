"""
    programa que muestra el manejo de operadores logicos
    dados por el ususario 
    Autor: kevin Aguirre
    Fecha: 20 de octubre de 2023   
"""

# los operadores logicos son: and, or, not

producto = input ('ingrese producto :')

#aca, si el producto es cualqier de los dos que no pague iva

print('--------super mercado--------')

if producto == 'lentejas' or producto == 'arroz' or producto == 'crema' or producto == 'vino':

    if producto == 'lentejas' or producto == 'arroz':
        print('no paga iva')
    else:
        print('paga iva')
else:
    print('ingrese un producto valido')
    

print('--------estrato y edad--------')

estrato = input ('ingrese estrato :')
edad = input ('ingrese edad :')

if estrato < 3 and edad >= 18:
    print('tiene derecho a subsidio')
else:
    print('no tiene derecho a subsidio') 
    
print('--------not None--------')

empezar = None #none se usa para indicar que una variable no posee un valor funcional 

if empezar is not None:
    print('la variable tiene un dato tipado')
else:
    print('la variable es None')
    
print('--------not True--------')

soltero = True
print(not soltero)
habilitado = False 
print(not habilitado)
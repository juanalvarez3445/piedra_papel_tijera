"""
    programa que muestra el manejo de condicionalesen python 3
    dados por el ususario 
    Autor: kevin Aguirre
    Fecha: 20 de octubre de 2023   
    """
    
# pedimos nombre, si nombre es maria la saludamos 
print('-------condicional doble---------')
nombre = input("ingrese nombre : ")
if nombre == 'maria' : 
    print ('hola mari')
else: 
    print ('usted no eres Maria')
        
print('------elif------')
        
estrato = int (input('ingrese el estrato : '))
if estrato == 1:
    print('usted tine derecho a subsidio completo')
elif estrato == 2:
    print('usted tiene derecho a medio subsidio')
else:
    print('usted no tiene derecho al subsidio')
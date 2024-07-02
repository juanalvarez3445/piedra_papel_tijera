"""
    programa para un prestamo
    dados por el ususario 
    Autor: juan carlos ceballos
    Fecha: 20 de octubre de 2023   
"""


nombre =  input ('ingrese su nombre :')
prestamo = float (input('ingrese la cantidad de prestamo :'))
plazo = float (input('ingrese el plazo de meses maximo :'))
intereses = prestamo * 0.27
total1 = prestamo / plazo
total2 = total1 + intereses 

print('------------factura-----------')

print (nombre)
print ('el interes de su prestamo es de :', intereses)
print ('las cuotas mensuales son de :', total2)
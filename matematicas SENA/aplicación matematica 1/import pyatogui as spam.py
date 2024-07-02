#enviar
import pywhatkit as spam 
import time 

limite = input('1000')
mensaje = input('estupido')

i = 0 

time.sleep(5)

while i<int(limite):
    spam.typewrite(mensaje)
    spam.press('enter')
    i+=1
    print('enviado')
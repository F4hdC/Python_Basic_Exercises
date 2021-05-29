# F4hdC ©

import string

# Guardo el input en una variable
inp = input("Introduce un texto: ")

# Variables como contadores
alf_low = 0
alf_upp = 0
acen_low = 0
acen_upp = 0
letras_raras = 0
espacios = 0

acentuados_low="áéíóúñ"
acentuados_upp="ÁÉÍÓÚÑ"

#loop for, y incremento los contadores
for x in inp:
    if(x in string.ascii_lowercase):
        alf_low+=1
    elif(x in string.ascii_uppercase):
        alf_upp+=1
    elif(x in acentuados_low):
        acen_low+=1
    elif(x in acentuados_upp):
        acen_upp+=1
    elif(x == ' '):
        espacios+=1
    else:
        letras_raras+=1

# Imprimo los resultados
print("Las minúsculas : {}".format(alf_low))    
print("Las Mayúsculas : {}".format(alf_upp))    
print("Las acentuadas en minúsculas : {}".format(acen_low))    
print("Las acentuadas en mayúsculas :",acen_upp)    
print("Espacios :",espacios)    
print("Otros caracteres :",letras_raras)    

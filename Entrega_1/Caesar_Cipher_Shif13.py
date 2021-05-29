# F4hdC ©

import string 

# obtengo mi lista de alfabetos desde la libreria string
alfabetos=(string.ascii_lowercase)

#guardo el input dentro de mi variable
inp=input("Introduce un texto: ")
inp=inp.lower()

for x in inp:  
    if(x in alfabetos):
        posicion=alfabetos.index(x)
        rot13=posicion+13
        if(rot13>25):
            rot13-=26
        x=alfabetos[rot13]
    elif(x==' '): # Detectar los espacios
         x=' '
    else: # En caso de que no exista la letra, Ex:'ñ', pongo un symbolo raro
        x="%"        
    print(x,end='')
    
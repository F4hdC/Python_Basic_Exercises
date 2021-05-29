# F4hdC ©

# Guardo el input en una variable
inp = input("HEX ?: ")
inp=inp.lstrip('#')
inp=inp.lower()

# Mi lista de alfabetos HEX
lista={"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}

# Mi lista de acentuados
acentuados_low={"á":'a',"é":'e',"í":'i',"ó":'o',"ú":'u',"ñ":'n'}

# Inicializo mis variables
r=g=b=0
i=0
rgb=[]
pasa=0
va=''

# Controlo si se meten 6 caracteres para validar el formato HEX, Si no se cumplen Salgo
if(len(inp)>6) or (len(inp)<6):
    print("Debes introducir 6 caracteres Ej: #ff17ca")
    quit()

# Cuando el programa llegue aquí, compruebo que todos los caracteres son válidos, si no, Muestro...
# Mensaje de error con la posicion y el caracter no válido y acaba el programa
x=0
while (x<len(inp)):
    if(inp[x] in lista) or (inp[x].isdigit()):
        pasa+=1
    else:
        if(inp[x] in acentuados_low):
             va = acentuados_low[inp[x]]
        else:
            va = inp[x]
        print("Caracter no válido: ["+va+"], su posicion es: {}".format(x+1))
    x+=1

# Aquí compruebo si todos los caracteres son válidos en el paso anterior o no
if(pasa<6):
    quit()

# Si llego aquí es porque todo ha ido bien
# Si es par, siginfica que es el caracter (0,2,4), los multiplico por 16
while (i < len(inp)):
    if (i%2==0):
        if(inp[i] in lista):
            rgb.append(lista[inp[i]]*16)
        elif(inp[i].isdigit()):
            rgb.append(int(inp[i])*16)
# Si es impar, significa que es el caracter (1,3,5), guardo su valor simplimente
    else:
        if(inp[i] in lista):
            rgb.append(lista[inp[i]])
        elif(inp[i].isdigit()):
            rgb.append(int(inp[i]))

    i+=1

# Aquí voy sumando los pares r,g,b
r=sum(rgb[0:2])
g=sum(rgb[2:4])
b=sum(rgb[4:6])

print("RGB: ("+format(r)+","+format(g)+","+format(b)+")")
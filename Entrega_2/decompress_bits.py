# F4hdC ©

# Guardo el input en una variable
inp = input("Introduce una cadena de bits: ")
x=0 # inicializo mi iterador 

if(inp.isdigit()):
    while (x<len(inp)):
        if(inp[x] != '0') and (inp[x] != '1'):
            for y in range(int(inp[x])):
                print(inp[x+1],end="")
            x+=2
        else:
            print(inp[x],end="")
            x+=1




            
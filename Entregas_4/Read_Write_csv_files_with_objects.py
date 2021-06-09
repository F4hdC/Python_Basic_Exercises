# F4hdC ©
class Alumno:
    nombre=""
    apellidos=""
    edad=""
    titulacion=""
    curso=""
    notaMedia=""


    def __init__(self, nombre, apellidos, edad, titulacion, curso, nota):
        """Constructor de clase Alumno"""
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.titulacion = titulacion
        self.curso = curso
        self.notaMedia = nota



nombres = []
apellidos = []
edades = []
titulaciones = []
cursos = []


import csv
import random

datos =  []
with open('alumno.csv') as File:
    reader = csv.reader(File, delimiter=';', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        nombres.append(row[0])
        apellidos.append(row[1])
        edades.append(row[2])
        titulaciones.append(row[3])
        cursos.append(row[4])

lista_objetos = []




for i in range(4):

    nota=random.randint(3,9)
    objeto = Alumno(nombres[i],apellidos[i],edades[i],titulaciones[i],cursos[i],nota)
    lista_objetos.append(objeto) 
    #globals()["obj" + str(i)] 

print("------------------------------------------------")
print("Todos los datos de cada objeto")
print("------------------------------------------------")

for i in range(len(lista_objetos)):
    print("nombre: ",lista_objetos[i].nombre, end=", ")
    print("Apellidos: ",lista_objetos[i].apellidos, end=", ")
    print("Edad: ",lista_objetos[i].edad, end=", ")
    print("Titulacion: ",lista_objetos[i].titulacion, end=", ")
    print("Curso: ",lista_objetos[i].curso, end=", ")
    print("NotaMedia: ",lista_objetos[i].notaMedia, end=" ")
    
    print("")

# creamos nuevo archivo

with open("Salida.txt","wt") as out:
    writer=csv.writer(out)
    #writer.writerow(('Nombre', 'Apellidos', 'Edad', 'Titulación','Curso','NotaMedia'))

    for j in range(len(lista_objetos)):
        row = (lista_objetos[j].apellidos,lista_objetos[j].nombre,lista_objetos[j].curso,lista_objetos[j].notaMedia)
        writer.writerow(row)

print("------------------------------------------------")
print("Datos escritos, Fichero de salida -> Salida.txt")
print("------------------------------------------------")

















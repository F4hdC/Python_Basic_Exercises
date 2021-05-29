# F4hdC ©
import csv
from matplotlib import pyplot as plt

result =[]
with open('datos.csv') as File:
    reader = csv.reader(File, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in reader:
        result.append(row)
    #print(result)


ventas = []
paises = []

for i in range(len(result)):
    ventas.append(int(result[i][1]))

for i in range(len(result)):
    paises.append(result[i][0])

print(ventas)

plt.pie(ventas,labels = paises,autopct='%1.2f%%',startangle=90)

plt.show()


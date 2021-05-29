# F4hdC ©
import csv

result =[]
with open('datos.csv') as File:
    reader = csv.reader(File, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in reader:
        result.append(row)
    print(result)


mx_mn_ventas = []

for i in range(4):
    mx_mn_ventas.append(int(result[i][1]))

mx_v = mx_mn_ventas.index(max(mx_mn_ventas))
mn_v = mx_mn_ventas.index(min(mx_mn_ventas))

print("El país con mayor venta es: ",result[mx_v][0])
print("Con un total de: "+result[mx_v][1])
print("*********************************************")
print("El país con mayor venta es: ",result[mn_v][0])
print("Con un total de: "+result[mn_v][1])
print("*********************************************")
print("La suma de ventas es:",sum(mx_mn_ventas))




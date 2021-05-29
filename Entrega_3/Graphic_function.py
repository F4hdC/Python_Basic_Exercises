# F4hdC ©
from matplotlib import pyplot

# Función cuadrática.
def f1(x):
    return (x**2)

# Función lineal.
def f2(x):
    return (x**3)
# Función lineal.
def f3(x):
    if x!= 0:
        return (1/x)

# Valores del eje X que toma el gráfico.
x = range(-10, 15)

# Graficar ambas funciones.
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
pyplot.plot(x, [f3(i) for i in x])

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
pyplot.xlim(-20, 20)
pyplot.ylim(-20, 20)

# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")

# Mostrarlo.
pyplot.show()
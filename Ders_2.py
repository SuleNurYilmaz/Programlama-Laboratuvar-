import sympy as sym
from sympy import Symbol,pprint
#%matplotlib notebook
import sympy.plotting as syp


sigma = Symbol("sigma")
mu = Symbol("mu")
x= Symbol("x")

part_1=1/sym.sqrt(2*sym.pi*sigma**2)
part_2=sym.exp(-1*((x-mu)**2)/(2*sigma**2))

my_gaussfunction=(part_1*part_2)
pprint(my_gaussfunction)

syp.plot(my_gaussfunction.subs({mu:1,sigma:3}),(x,-10,10),title="gauss distribution")



x_values=[]
y_values=[]
for value in range(-50,50):
    y=my_gaussfunction.subs({mu:0,sigma:10,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

# %matplotlib inline
import matplotlib.pyplot as plt

plt.plot(x_values,y_values)

plt.show()
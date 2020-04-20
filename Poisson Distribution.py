#Şule Nur Yılmaz 170401058
#

""" Poisson Distribution: Bir olayın belirli bir süre içinde ortalama gerçekleşme sayısı bilinerek verilen (olasılığı hesaplanmak istenen) olay sayısının gerçekleşme  olasılığının hesaplanması """

from sympy import Symbol, exp, factorial, pprint
import sympy.plotting as  syp
import matplotlib.pyplot as pyp



x = Symbol("x")  #Gerçekleşmesi beklenen sayı
lamda = Symbol("lamda")  #Nadir bir olayın belli bir süredeki gerçekleşme ortalaması


expr = (exp(-lamda)*(lamda)**x)/factorial(x)  #Gerçekleşme olasılığını veren ifade
pprint(expr)

syp.plot(expr.subs({lamda:5}),(x,0,50),title="Poisson Distribution lamda=5")


x_values=[]
y_values=[]
for value in range(0,51):
    y=expr.subs({lamda:5,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)

pyp.plot(x_values,y_values)
pyp.title("Poisson Distribution lamda=5")
pyp.show()
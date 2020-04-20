from sympy import Symbol, exp, factorial
import sympy.plotting as  syp
import matplotlib.pyplot as pyp

"""Kullanıcıdan bir olayın kaç ay süre için ortalama kaç kez gerçekleştiği ve kaç ay için kaçla kaç arası olayın gerçekleşmesi olasılığını istediği alınıp geriye olasılıklarını veren grafik """

x = Symbol("x")
lamda = Symbol("lamda")

expr = (exp(-lamda)*(lamda)**x)/factorial(x)
flag=False
flag2=False
kaza=list()
while flag==False:
    try:
        ay_user=int(input("Kaç ay üzerinden ortalama alınmıştır: "))
        kaza_user=int(input("Olay ortalama Kaç kez olmuştur: "))
        ay_2=int(input("Kaç ay üzerinden hesaplanmak isteniyor: "))
        print("Olay sayısının hangi aralık değerlerinde olma olasılığı isteniyor : ")

        for i in range (0,2):
            while flag2==False:
                try:
                    kaza_2=int(input("{}. : ".format(i+1)))
                    kaza.append(kaza_2)
                    break
                except ValueError:
                    print("Sadece sayı giriniz!")

        break
    except ValueError:
        print("Sadece sayı giriniz!")

if ay_user ==ay_2:
   syp.plot(expr.subs({lamda:kaza_user}), (x, kaza[0], kaza[1]), title="Poisson Distribution")
else:
    x_values = []
    y_values = []
    for value in range(kaza[0], kaza[1]):
        y = expr.subs({lamda: kaza_user, x: value}).evalf()
        y_values.append(y)
        x_values.append(value)

    pyp.plot(x_values, y_values)
    yeni = (ay_2 * kaza_user) / ay_user
    x_values_2 = []
    y_values_2 = []
    for value in range(kaza[0], kaza[1]):
        y = expr.subs({lamda: yeni, x: value}).evalf()
        y_values_2.append(y)
        x_values_2.append(value)

    pyp.plot(x_values_2, y_values_2)
    pyp.title("Poisson Distribution Comparison")

    pyp.show()

    """syp.plot(expr.subs({lamda: kaza_user}), (x, kaza[0], kaza[1]), title="Poisson Distribution")
    yeni= (ay_2*kaza_user)/ay_user
    syp.plot(expr.subs({lamda: yeni}), (x, kaza[0], kaza[1]), title="Poisson Distribution")
    """
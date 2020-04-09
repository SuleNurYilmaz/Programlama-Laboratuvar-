from sympy import Symbol, factor,expand,pprint

x = Symbol("x")
y = Symbol("y")

p = x*(x+x)
print(p)

p = (x+2)*(x+3)
print(p)

expr = x**2 - y**2
print(factor(expr))
print(expand(factor(expr)))

print((x+y)**3)
pprint((x+y)**3)


x = Symbol("x")
series = x
n=5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)


expr = x*x + x*y + x*y + y*y

res = expr.subs({x:1, y:2})
print(res)

r= expr.subs({x:1-y})
print(r)

#04.03.2020


#170401058

my_d =dict()

def my_h(liste):
    for i in liste:
        if i in my_d:
            my_d[i]=my_d[i]+1
        else:
            my_d[i]=1
    return my_d

def lookup(d,v):
    for k in d:
        if d[k]==v:
            return k
    return -1

def fibo_rec(n):
    if n<2:
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)

known = {0:0,1:1}

def fibo_rec2(n):
    if n in known:
        return known[n]
    else:
        result = fibo_rec2(n-1)+fibo_rec2(n-2)
        known[n]=result
        return result

#06.03.2020

def my_h2(liste):
    my_d={}
    for item in liste:
        if item not in my_d:
            my_d[item]= 1
        else:
            my_d[item]=my_d[item]+1
    return my_d

def look_up2(d,v):
    for key in d:
        if d[key]==v:
            return key
        else:
            return -1

def probability(space,event):
    return len(event)/len(space)


def check_prime(number):
    if number !=1:
        for factor in range(2, number):
            if number % factor == 0
                return False
    else:
        return False
    return True

space=finiteSet(*range(1,21))
primes=[]
for num in space:
    if check_prime(num):
        primes.append(num)
    event = finiteSet(*primes)
    p = probability(space,event)
    print(p)
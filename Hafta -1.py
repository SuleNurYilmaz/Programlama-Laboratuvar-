#19.02.2020

#170401058


def power1(a,b):
    if b == 0:
        return 1
    elif b==1:
        return a
    else:
        if b%2 == 0:
            return power1(a*a,b//2)
        else:
            return power1(a*a,b//2)*a

def power2(a,b):
    if b==0:
        return 1
    elif b ==1:
        return a
    else:
        t=1
        for i in range(b):
            t = t*a
            return t

def power3(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    if b>1:
        return power(a,b-1)*a

def my_d_1():
    liste=[4,-3,5,-2,-1,2,6,-2]
    max = 0
    for i in range(8):
        for j in range (i+1,8):
            t =0
            for k in range(i,j+1):
                t = t + liste[k]
            if t > max:
                max = t
                i1,i2=i,j
    return max,i1,i2

#21.02.2020

def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_sub_sum_recursive(list = [4,-3,5,-2,-1,2,6,-2]):
    if len(list)==1:
        return list[0]
    n = len(list)
    left_i = 0
    left_j = n//2
    right_i = n//2
    right_j = n

    left_sum = my_sub_sum_recursive(list[left_i:left_j])
    right_sum = my_sub_sum_recursive(list[right_i,right_j])

    t,temp_left_sum = 0,0
    for i in range(left_j,left_i,-1):
        t = t+ list[i]
        if(t> temp_left_sum):
            temp_left_sum = t

    t,temp_right_sum = 0,0
    for i in range(right_i,right_j):
        t = t+list[i]
        if(t>temp_right_sum):
            temp_right_sum = t
    center_sum = temp_left_sum + temp_right_sum

    return max_of_three(left_sum,right_sum,center_sum)

def my_bubble(liste):
    for i in range(len(liste)-1,-1,-1):
        for j in range(i):
            if liste[j]> liste[j+1]:
                t= liste[j+1]
                liste[j+1]=liste[j]
                liste[j]=t
    return liste


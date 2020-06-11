#26.02.2020

#170401058

def my_fonk_1(liste):
    n = len(liste)
    maxsum = 0
    for i in range(n):
        for j in range(i, n):
            t = 0
            for k in range(i,j):
                t = t + liste[k]
            if (t > maxsum):
                maxsum = t
    return maxsum

def my_fonk_2(liste):
    n = len(liste)
    maxsum=0
    for i in range(n):
        t = 0
        for j in range(i,n):
            t= t+liste[j]
            if(t > maxsum):
                maxsum = t
    return maxsum


def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def my_fonk_3(list = [4,-3,5,-2,-1,2,6,-2]):
    if len(list)==1:
        return list[0]
    n = len(list)
    left_i = 0
    left_j = n//2
    right_i = n//2
    right_j = n

    left_sum = my_fonk_3(list[left_i:left_j])
    right_sum = my_fonk_3(list[right_i,right_j])

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

#28.02.2020

def insertionSort(arr):
    n= len(arr)
    for i in range(1,n):
        key= arr[i]
        j= i-1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1]= key

def shellsort(arr):
    n=len(arr)
    gap = n//2
    while gap >0:
        for i in range(gap,n):
            temp =arr[i]
            j=i
            while j>= gap and arr[j-gap] > temp:
                arr[j]= arr[j-gap]
                j= j-gap
            arr[j]= temp
        gap //=2


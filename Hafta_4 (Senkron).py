def min_heapify(array,i):
    left = 2 * i +1
    right = 2 * i +2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest =left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array,smallest)

def build_min_heap(array):
    for i in reversed(range(((len(array))//2))):
        min_heapify(array,i)

my_array_1=[8,10,3,4,7,14,1,2,16]

build_min_heap(my_array_1)

print(my_array_1)

def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array =[]
    for i in range(len(array)):
        array[0],array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array

my_array=[8,10,3,4,7,15,1,2,16]
my_array_2=heapsort((my_array))

print(my_array_2,my_array)

#######################################################################

myheap=[8,10,3,4,7,14,1,2,16]
build_min_heap(myheap)
print(myheap)

def up_heap(myheap_1,index):
    x = (index-1)//2
    if x>=0 and myheap_1[x] > myheap_1[index]:
        myheap_1[x],myheap_1[index]=myheap_1[index],myheap_1[x]
        up_heap(myheap_1,x)

def insertItemToHeap(myheap_1,item):
    myheap_1.append(item)
    myheap_1 =up_heap(myheap_1,myheap_1.index(item))

def removeItemFrom(myheap_1):
    if len(myheap_1):
        x = myheap_1[0]
        myheap_1[0]=myheap_1[-1]
        myheap_1.pop()
        min_heapify(myheap_1,0)
        return x
    else:
        return 1000000000

insertItemToHeap(myheap,0)
print(myheap)

print("çıkarılan:",removeItemFrom(myheap))
print(myheap)
print("çıkarılan:",removeItemFrom(myheap))
print(myheap)
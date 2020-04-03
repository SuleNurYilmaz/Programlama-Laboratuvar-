import random

### Generate List With n Items ###

# random.random()  0-1 arası float sayı verir.
print("random.random() kullanımı: ",random.random(),sep="\n")

# random.randint(1,100) 1-100 arası (1 ve 100 dahil) rastgele int sayı verir.
print("random.randint(1,100) kullanımı: ",(random.randint(1,100)),sep="\n")

def get_n_random_numbers(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers

print("get_n_random_numbers() kullanımı: ",get_n_random_numbers(),sep="\n",end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Histogram With Two Methods ###

# for a list [0,-4,8,-1,0,-3,6,3,0,1]
# get the histogram, with arrey of tuples format
# Örnek histogram modeli:
histogram_1=[(-4,1),
             (-3,1),
             (-1,1),
             (0,2),
             (1,1),
             (3,1),
             (6,1),
             (8,1)]

my_list = get_n_random_numbers(10,-4,4) # Liste Üretildi.

print("Üretilen Liste: ",my_list,sep="\n")

my_list = sorted(my_list) # Liste Sıralandı.

print("Sıralanan Liste: ",my_list,sep="\n")

def my_frequency_with_dict(list):
    frequency_dict={} # dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict

print("Sözlük yardımıyla oluşturulan histogram: ",my_frequency_with_dict(my_list),sep="\n")

def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[] # list()=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list
print("Tuple(demet) yardımıyla oluşturulan histogram: ", my_frequency_with_list_of_tuples(my_list),sep="\n")

result_1=my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)


print("Dict ile histogram: "+str(result_1),"Liste ile histogram: "+str(result_2),sep="\n",end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Mode of a List With Histogram ###

my_list_1=get_n_random_numbers(10)
my_hist_d=my_frequency_with_dict(my_list_1)

print("Histogram (dict) : ",my_hist_d,sep="\n")

my_hist_l=my_frequency_with_list_of_tuples(my_list_1)

print("Histogram (tuple) : ",my_hist_l,sep="\n")


# to get mode, we have to search all keys on hist_dict

frequency_max=-1  # mode değeri, döngüde karşılaştırılacak hafıza amaçlı değer
mode=-1
for key in my_hist_d.keys():
    #print(key,my_hist_d[key],end=" || ")  sözlükteki anahtarların değerlerini döndürüyor.
    if my_hist_d[key]>frequency_max:
        frequency_max=my_hist_d[key]
        mode=key
print("Verilen listede dict histogramı kullanılarak mode bulma : frekans -> {} mode -> {} ".format(frequency_max,mode))

# Dict histogramı ile Mode bulma fonksiyonu

def my_mode_with_dict(my_hist_d):
    frequency_max = -1
    mode = -1
    for key in my_hist_d.keys():
        #print(key, my_hist_d[key])
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode, frequency_max

print("my_mode_with_dict fonksiyon kullanımı: ",my_mode_with_dict(my_hist_d))


my_list_100=get_n_random_numbers(10,-40,40)
my_hist_100_d=my_frequency_with_dict(my_list_100)
print("Fonksiyon denemesi 2: ", my_mode_with_dict(my_hist_100_d),end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Mode of a List With Histogram ( a List of Tuples) ###

my_list_1=get_n_random_numbers(10)
my_hist_list=my_frequency_with_list_of_tuples(my_list_1)

print("Histogram (Tuple): ",my_hist_list,sep="\n")

# to get mode, we have to search all keys on hist_list

frequency_max=-1
mode=-1
for item,frequency in my_hist_list:
    #print(item,frequency)
    if frequency>frequency_max:
        frequency_max=frequency
        mode=item
print("Verilen listede tuple histogramı kullanılarak mode bulma : frekans -> {} mode -> {} ".format(frequency_max,mode))

# List histogramı ile Mode bulma fonksiyonu

def my_mode_with_list(my_hist_list):
    frequency_max = -1
    mode = -1
    for item,frequency in my_hist_list:
        # print(item,frequency)
        if frequency > frequency_max:
            frequency_max = frequency
            mode = item
    return mode,frequency_max

print("my_mode_with_list fonksiyon kullanımı: ",my_mode_with_list(my_hist_list))


my_list_100=get_n_random_numbers(10,-40,40)
my_hist_100_l=my_frequency_with_list_of_tuples(my_list_100)
print("Fonksiyon denemesi 2: ", my_mode_with_list(my_hist_100_l),end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Linear Search on List ###


def my_search_1(my_list,item_search):
    found=(-1,-1)   # default, eğer listede yoksa
    for indis in my_list:
        if indis ==item_search:
            found=(indis,my_list.index(indis))    # listede bulundu, return bulunan sayı, indisi tuple olarak return edilir.

    return found

print("Liste: ", my_list,"Lineer Aramada Listedeki 3 Sayısının Bulunması: ",my_search_1(my_list,3),sep="\n")


def my_search_2(my_list,item_search):
    found=(-1,-1)   # default, eğer listede yoksa
    n=len(my_list)
    for indis in range(n):
        if my_list[indis] ==item_search:
            found=(my_list[indis],indis)    # listede bulundu, return bulunan sayı, indisi tuple olarak return edilir.
            # break, uncomment for last found
    return found

print("Liste: ", my_list,"Lineer Aramada Listedeki 3 Sayısının Bulunması: ",my_search_2(my_list,3),sep="\n",end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Mean of List ###

print("Liste: ", my_list)

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean=t/s
    return mean

print("Listenin Ortalaması :",my_mean(my_list),end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Sort The List ###

my_list=get_n_random_numbers(10,-4,4)
print("Liste: ",my_list)

def my_bubble_sort(my_list):
    n=len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j]<my_list[j+1]):
                #Swap İşlemi
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

print("Kabarcık Sıralaması:",my_bubble_sort(my_list),end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Binary Search on a Sorted List ###

def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1

    while low <= high:
        mid = (low + high) // 2

        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found

my_list_1=get_n_random_numbers(10)
print("Liste: ", my_list_1)
my_list_2=my_bubble_sort(my_list_1)
print("Sıralı Liste: ", my_list_2)
print("Binary Search ile Listede 3 sayısının bulunması: ",my_binary_search(my_list_2,3),end=2*"\n"+50*"#"+2*"\n")


###########################################################################################


### Median of a List ###

size=input("dizi boyutunu giriniz")
size=int(size) #convert str to int
my_list_1=get_n_random_numbers(size)

print("Liste: ",my_list_1)

my_list_2=my_bubble_sort(my_list_1)
print("Kabarcık sıralaması ile sıralanan liste: ", my_list_2)

def my_median(my_list):
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)
        median=my_list_2[middle]
        return median
    else:
        middle_1=my_list_2[int(n/2)-1]
        middle_2=my_list_2[int(n/2)]
        median=(middle_1+middle_2)/2
        return median

print("Liste: ",my_list_2,"Ortanca: ",my_median(my_list_2))
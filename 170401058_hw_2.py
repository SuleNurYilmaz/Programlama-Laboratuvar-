import sys,os

a=os.getcwd()

def histogram():    #   Histogram oluşturma
    with open("{0}/{1}/input_hw_2.csv".format(a,sys.argv[1]),"r") as veri:
        text=veri.readlines()
    liste=[]
    flag= False
    for x in text:
        x=x.rsplit("-",2)
        flag = False
        for eleman in liste:
            if x[1] == eleman[0]:
                liste[liste.index(eleman)][1]+=1
                flag= True
                break
        if flag is False:
            liste.append([x[1],1])
    return liste

def sort(liste):    #   Liste sıralama
    for i in range(len(liste)-1,-1,-1):
        for j in range(0,i):
            if liste[j][1]>liste[j+1][1]:
                temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=temp
    return liste

def medyan(lis):    #   Medyan bulma
    liste=sort(lis)
    if len(liste)%2==0:
        index=len(liste)//2
        return (liste[index][1]+liste[index-1][1])/2
    else:
        index=len(liste)//2
        return liste[index][1]

def ortalama(liste):    #   Ortalama bulma
    toplam=0
    for i in liste:
        toplam+=i[1]
    return toplam/len(liste)

def output(liste):  #   Verileri dosyaya yazdırma
    with open(r"{}\{}\170401058_hw_2_output.txt".format(a,sys.argv[2]),"w") as output:
        output.write("Medyan: {} \n".format(medyan(liste))+"Ortalama: {} \n".format(ortalama(liste)))


try:
    output(histogram())
    print("İşlem Başarılı!")
    exit()
except IndexError as hata:
    print("Hata: {} \n ".format(hata),
          "Kullanım: python 170401058_hw_2.py input_dir_name output_dir_name")
except FileNotFoundError as hata:
    print("Hata: {} ".format(hata))
    print("Kullanım: python 170401058_hw_2.py input_dir_name output_dir_name")
finally:
    print("Program Kapatılıyor...")

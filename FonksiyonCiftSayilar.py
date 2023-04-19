sayi=int(input("bir sayi giriniz"))
def CiftSayilar(x):
    liste=[]
    for i in range(1,sayi+1,1):
        if i%2==0:
            liste.append(i)

    return liste

print(CiftSayilar(sayi))
import random
RandomSayi=round(random.random()*100)
print(RandomSayi)
GirilenSayi= int(input("0-100 arasinda bir sayi giriniz: "))
while RandomSayi != GirilenSayi:
    if GirilenSayi>RandomSayi:
        print("Buyuk Bir Sayi Girdiniz")
    else:
        print("Kucuk Bir Sayi Girdiniz")
    GirilenSayi= int(input("0-100 arasinda bir sayi giriniz: "))
print("kazandiniz")
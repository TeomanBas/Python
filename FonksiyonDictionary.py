def fonksiyon(**a):
    for i in a:
        print(str(i) + " => " + str(a[i]))
# aslinda bir dictionary tanımladik yani a b ve c indislerinin degerlerini tanimladik 
# ** ifadesi ile tum parametreleri ekledik.
fonksiyon(a=2,b=3,c=4,d=5,e="sozluk")
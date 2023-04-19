# bir fonksiyon tanimlarken girilecek parametrelerin sayisi belli olmayabilir. 
# fonksiyon parametresini tutacak degiskenin basina * isareti konularak girilecek tum parametreler bir degiskende tutulabilir.

def topla(*a):
    for i in a:
        print(i)

topla(1,2,4,566,23,00,"bb","3adsf")

print("------------------------------------")


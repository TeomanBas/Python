sayi=int(input("sayi giriniz"))
us=int(input("us giriniz"))

sonuc=1
for i in range(1,us+1,1):
    sonuc*=sayi
print(sonuc)
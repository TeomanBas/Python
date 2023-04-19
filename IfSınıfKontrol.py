a_sinif=["ahmet","Mehmet"]
b_sinif=["ali","veli"]
isim=input("isim seciniz")
if isim in a_sinif:
    print("kisi a sinifinda")
elif isim in b_sinif:
    print("kisi b sinifinda")
else:
    print("kisi herhangi bir sinifta degil")
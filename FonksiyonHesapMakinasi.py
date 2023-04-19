def HesapMakinasi(x,y,z):
    if z==1:
        sonuc=x+y
    elif z==2:
        sonuc=x-y
    elif z==3:
        sonuc=x*y
    elif z==4:
        sonuc=x/y
    else:
        sonuc="hata"
    return sonuc
print(HesapMakinasi(1,2,3))
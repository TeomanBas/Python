metin=input("metin giriniz :    ")
liste=list(metin)
harf=0
rakam=0
for i in liste:
    if str(i).isdecimal():
        rakam+=1
    else:
        harf+=1
print("harf : ",harf)
print("rakam : ",rakam)

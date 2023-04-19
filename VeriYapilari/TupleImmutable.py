list=[1,2,3]
tuple=(1,2,3)
print(list)
print(tuple)
# tuple ve listenin farkı listenin degistirilebilir olmasi ve tuplenin degistirilemez olmasidir.ve parantez tanimlanir.
list[0]=99
# tuple[0]=99 # bu kisim hata almamıza neden olur.
print(list)
print("----------------------")
print(tuple)
print("----------------------")
# bu sekildede tuple tanimlayabiliriz.Tuple oldugunu ise yazdirildiginda parantez icerisinde bulunmasindan anlayabiliriz.
t2=1,2,3
t3='A','B','C'
print(t2)
print(t3)
print("----------------------")
# tuple lari su sekilde degistiririz
# 1- tuple icerisindeki değerleri x y z degiskenlerine atadık.
x,y,z=tuple
print(x)
print(y)
print(z)

# 2- x degerini degistirmemiz tuple degerini degistirmeyecek cünkü x kendi basina bir degisken tuple icerisindeki degisken degil
# biz x y z degiskenlerini tupleye esitleyerek sadece x y z degiskenlerine tuple daki degerleri verdik. Bu tuple i etkilemedi

x=99

print(tuple)

# 3- tuple degiskeninin degistirmek istiyorsak sifirdan bir tuple degeri degeri atamamız gerekiyor.
tuple=(x,y,z)
print(tuple)
print("---------------------------------------------------")

# 4- tuple icerisine listeler de tanimlayabiliriz Ve bu listelerin icerisinde degisiklik yapabiliriz Ama tuple yine 
# iki liste göstermis olacak onu degistiremeyiz.tuple icerisindeki listeler listeler dünyasına aittir ve listelerin
# kurallari ve esnekleri ile kullanilabilirler.

tuplelist=([50,60,70],[80,90,100])
print(tuplelist)
# [0] => tuplelist in sifirinci elemani
print(tuplelist[0])
# [0][2] => tulelist in sifirinci elemaninin ikinci elemani
print(tuplelist[0][2])
tuplelist[0][2]=11111
#aynı tuplelist ancak farklı bir liste
print(tuplelist)





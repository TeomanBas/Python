# Side Effect (yan etki)
# bir for dongusu icerisinde 1 den 10 a kadar olan sayilari yazdirmak istersek en az bir tane degiskene ihtiyacımız olur
# halbuki asıl amacimiz sadece sayilari yazdirmakti.başka kod bloklarinin kodlarinin arasinda da ayni sekilde bu tur bir 
# tanimlama yapilirsa diger foksiyon yada parametreleri etkiler bunun onune gecmek icin ise her isin yapildigi kod bloklarinda 
# farkli parametreler tanimlamamız gerekmektedir ve buda bizim icin çok buyuk bir problem olur.
# bunun onune gecmek icin lamda tanimlaması yapılır lamda islem bitene kadar degiskeni tanimlar islem bitince degiskeni 
# siler yani bir cok farkli fonksiyon icerisinde ayni degiskenleri kullanarak fazladan degiskenler olusturmadan islemlerimizi
# yurutebiliriz.
l=[]
for x in range(1,20):
    l.append(x**2)

print(l)

print("görüldüğü gibi fazladan bir x değişkenimiz oldu => " + str(x))
print("---------------------------------------------------------------------------")

def f(x):
    return x+5

l2=[1,2,3]

# map() fonksiyonu bir liste icindeki herbir eleman icin istedigimiz bir fonksiyonu uygular
# list() fonksiyonu dizi elemanlarini alir ve bunlari listelere donusturur.
# lambda ile yukarıda bahsettigim uzere gecici bir deger olusturur
print(list(map(f,l2)))
print("map fonksiyonu l nin degerlerini etkilemedi =>" + str(l2))
print("--")
print(list(map(lambda x:x+5,l2)))





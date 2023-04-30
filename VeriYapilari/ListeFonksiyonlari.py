print("")
print("append islemi------------------------------------------")
print("")
a=[1,2,3,4,5]
print(a)
a.append('a')
# append liste icerisine yeni eleman ekler
print(a)
print("-------------------------------------------------------")
print("-------------------------------------------------------")



print("")
print("insert islemi------------------------------------------")
print("")

a.insert(0,'eklenen eleman')
# a.insert(sira,'eklenecek eleman') belirtilen siraya yeni eleman ekler
print(a)

print("-------------------------------------------------------")
print("-------------------------------------------------------")



print("")
print("remove islemi------------------------------------------")
print("")

# a.remove('silinecek eleman') ilk gordugu elemani siler hepsinin silinmesi için birden cokkez cagrilabilir.
a.append('silinecek eleman')
a.append('silinecek eleman')
print(a)
a.remove('silinecek eleman')
print(a)
a.remove('silinecek eleman')
print(a)

print("-------------------------------------------------------")
print("-------------------------------------------------------")




print("")
print("pop islemi------------------------------------------")
print("")

a.append("pop fonksiyonu")
print(a)
# a.pop() son eklenen degeri cikartir.stack(yigin yapisi) yapisina pop ve append (push metodu) ile kullanıbiliyoruz.
# pop metodu hem siler hemde en son elemani geri almaya yarar.
a.pop()
print(a) 

print("-------------------------------------------------------")
print("-------------------------------------------------------")



print("")
print("index islemi------------------------------------------")
print("")
# a.index(sira sayisi) index metodu sira numarasi girilen bir elemanin ne oldugunu gosterir yani index ten eleman bulur.
print("2 numarali indexteki eleman : " +str(a.index(2)))

print("-------------------------------------------------------")
print("-------------------------------------------------------")




print("")
print("count islemi------------------------------------------")
print("")
# count() girilen degerden kac tane oldugunun sayisini verir 
a.append('a')
a.append('a')
print(a)
print("a dan " + str(a.count('a')) + " tane var")

print("-------------------------------------------------------")
print("-------------------------------------------------------")
 


print("")
print("sort islemi------------------------------------------")
print("")
# sort orjinal listeyi kalıcı olarak sıralar yani degistirir sorted ise sıralanmis bicimini gosterir.
b=[8,9,5,6,4]
print(b)
b.sort()
print(b)

print("-------------------------------------------------------")
print("-------------------------------------------------------")


print("")
print("reverse islemi------------------------------------------")
print("")
# reverse listeyi tersten siralamak icin kullanılabilir.
b=[8,9,5,6,4]
print(b)
b.sort()
print(b)
b.reverse()
print(b)

print("-------------------------------------------------------")
print("-------------------------------------------------------")


print("")
print("extend islemi------------------------------------------")
print("")

# a.extend(b) listeleri birlestirir. a listesi kalıcı olarak degisti. b ise ayni kaldi. a yi b listesi ile guncelledi.
print(a)
print(b)
a.extend(b)
print(a)
print(b)

# b.clear() b listesini temizler listenin kendisi silinmez sadece içerigi silinir.
b.clear()
print(b)

print("-------------------------------------------------------")
print("-------------------------------------------------------")


print("")
print("copy islemi------------------------------------------")
print("")
# copy() kopyalamanin iki farkli yolu vardir birisi shadow copy (gölge kopyasi) digeri ise deep copy dir
# shadow copy de içeriklerin birbirini göstermesi yani l1=l2 demektir. l1 ve l2 de tutulan veriler hafizada aynı verileri gosterir
# yani birisinde yapilan bir değişiklik diğerini etkiler ikisinin farklı veriler üzerinden çalışan kopyalar olması
# için l1=l2.copy() seklinde bir ifade ile kopyalanması gerekir.

m1= [5,9,7,3,4,7,6]
m2=m1.copy() # deep copy
m1.append('12345')
print(m1)
print(m2)

print("-------------------------------------------------------")
print("-------------------------------------------------------")
l=[1,2,3]
l.append(55)
print("son eklenen eleman silindi =>"+ str(l.pop()))
print(l)
print("son eklenen eleman silindi =>"+ str(l.pop()))
print(l)
print("------------------------------------------------------")
l1=[11,22,33,44]
l1.append(55)
print(l1)
#pop 0 denildiğinde 0 ıncı elemenı alıp listeden atar.
print("sifirinci eleman listeden atildi => " +str(l1.pop(0)))
#del l1[0]
#print(l1.popleft())
print(l1)

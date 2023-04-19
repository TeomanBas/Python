#dosya okuma yazma
f=open('dosya.txt','w')
f.write('Yurtta Sulh Cihanda Sulh.\n')
f.close()
f=open('dosya.txt','r')
print(f.read())
f.close()
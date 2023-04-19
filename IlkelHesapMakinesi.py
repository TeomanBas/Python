islem=input("islem seciniz");
sayi1=int(input("sayi1:*"));
sayi2=int(input("sayi2:*"));
if islem=="1":
    sonuc=int(sayi1)*int(sayi2);
    print(sonuc);
elif islem=="2":
    sonuc=int(sayi1)/int(sayi2);
    print(sonuc);
elif islem=="3":
    sonuc=int(sayi1)+int(sayi2);
    print(sonuc);
elif islem=="4":
    sonuc=int(sayi1)-int(sayi2);
    print(sonuc);


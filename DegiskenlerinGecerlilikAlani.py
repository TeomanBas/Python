def scope_test():
    def do_local():
        # herhangi bir tanimlama yok ise local degiskendir sadece bulundugu fonksiyon icinde tanimlidir.
        spam = "local spam"
    def do_nonlocal():
        # nonlocal tanimlamasi yapilirsa tum scope_test fonksiyonu icerisinde gecerlidir.
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        # global olarak tanimlanmis spam degiskeni tum fonksiyonların disinndan cagirilabilir.
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
    #fonksiyon icerisinde fonksiyon cagirabiliyoruz.bunada oz yineli yaklaşım(recursive yaklasim denilmektedir.)

print(fact(5))


# y=3 dendiğinde y nin default değeri 3 dür taki fonksiyona y parametresi için bir değer girildiğinde
def g(x,y=3):
    return x*y

print (g(2))
print (g(2,5))
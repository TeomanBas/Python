l3=[z**2 for z in range(10)]
# burada for z ler icin 0 dan 10 a a kadar olan sayilari z nin icine at ve z nin karesini al anlaminda kullaniliyor.
print(l3)
print("---------------------------------------------------------------------------")
# matris yapisi
l4=[(a,b,c) for a in [1,2,3] for b,c in [(1,2),(2,3),(3,4) ] if a != b ] 
print(l4)

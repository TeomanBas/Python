# matris diye tabir edilebilir aslı 'list of list' dir listeler listesi

l=[1,2,3]
m=[[1,3,5,6],[3,4,5],l] 

print(m)
print("-------------------------------------------------------------------")
l[1]=100
print(m)

k=[[[1,2],[3,6],[5,8,9]],[1,[3,8,5,0]],[[1,1]]]
print(k)
print(len(k))
print(k[1])

mt=[[row[i] for row in m] for i in range(3)]
print("---------------------------------------------------------------------")
print(mt)
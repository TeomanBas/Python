for i in range(1,100):
    bolunurmu=False
    for b in range(2,i):
        if(i%b==0):
            bolunurmu=True
            print(str(i)+"asal değil")
            break
            
    if (bolunurmu!=True):
        print(str(i)+"asal")


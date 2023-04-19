print("Liste-Kayit-Kume-Tanimlamasi--------------------------------------")
l=[1,2,3,1,2,3,4,5] # liste
t=(1,2,3,1,2,3) # kayit
k={1,2,3,1,3,2,5,1,4} # kumeler 

print(l)
print(t)
print(k)
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")
print()
print()

print("Set-Fonksiyonu----------------------------------------------------")
print("set fonksiyonu icine bir liste alip bu listenin elemanlarini kumeye cevirir.")
k2=set(l)
k3=set([1,2,3,1,2,3])
print(k2)
print(k3)
k4=set("Matematik")
k5=set("Geometri")
print(k4)
print(k5)
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")
print()
print()

print("Operatorler-------------------------------------------------------")
print(" | operatoru union yani birlesim ozelligidir.baska dillerde or diyede gecer")
print(k4|k5)
print(" - operatoro kume olarak tanimlanan degikenlerin kume farkini almaya yarayan bir operatordur.set differences")
print(k4-k5)
print(" & kumelerde kesisim operatorudur.")
print(k4&k5)
print(" ^ iki tarafli set differences alir yani iki tarafli farki alir iki kume icin birbirine olan farkidir. exclusive or")
print(k4^k5)
print("------------------------------------------------------------------")


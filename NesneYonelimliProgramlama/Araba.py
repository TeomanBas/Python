class araba:
    hiz=0
    renk=""
    modeli=""
    def hizlan(self):
        self.hiz=self.hiz + 1

x=araba()
print("arabanin hizi : ", x.hiz)
x.hiz=100
x.hizlan()
print("arabanin hizi : ", x.hiz)

y=araba()
y.hiz=70
y.hizlan()

print("y arabasinin hizi", y.hiz)

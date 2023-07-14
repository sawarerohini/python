# polymorphysm
# herarical
# methodoverloding :in wich same name but diffrent parameter is colled method overloding
# it does not sport python
# methodoverriding : in wich same method name same parameter but diffrent implimentation
class Calculater: #base class
    num1 = 100 # features
    num2 = 50

    def Calculation(self):
        print("will Calculate")

class Addition(Calculater): # chaild class derived
    def add(self):
        print(self.num1+self.num2)

class Substraction(Calculater):    #chaild class derived
    def Calculation(self):   #same method name same parameter but diffrent implimention
        print(self.num1-self.num2)   # changing implimentation

a1 =Addition() #object of chaild class addition
s1=Substraction()  # object of substraction class

a1.Calculation()
s1.Calculation()

# creat one class area(base class)in that area class create one method calculat area then crat 3 chaild class(rectangle (l*w),trangle(1/2(b*h),squre(a2)
#in 3 chaild class redefine area method and calculat area of that chaild class(shapes)

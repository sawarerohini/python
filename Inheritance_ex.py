# inheritance:
# supperclass (parent class,base)
# derived class (child class)
# aquring features & functionality to other class.
# 1)single level inheritance
class parent:
    surname ="saware"

class chaild(parent):
    name ="rohini"

    def show(self):
        print(self.name,self.surname)  # accesing deta member to parent class
ch1= chaild()
ch1.show()

# 2)multi level inheritance
class gparents:
    surname ="patil"
class parent(gparents):
    name = "bhagayshri"
class chaild1(parent):
    middle_name = "dnyanashwer"
    def show(self):
        print(self.surname,self.name,self.middle_name)
ch2= chaild1()
ch2.show()



class bsis:
    big_sis= "ashu_dii"
class msis(bsis):
    middle_sis = "usha_dii"
class lsis(msis):
    little_sis = "rohini"
    def show(self):
        print(self.big_sis,self.middle_sis,self.little_sis)
r = lsis()
r.show()

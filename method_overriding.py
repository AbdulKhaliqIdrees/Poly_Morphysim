#Method Overriding
class Math(object):
    def add(self,a,b):
        sum=a+b
        print("The Answer of Math:",sum)
class Stat(Math):
    def add(self,x,y):
        super().add(11,10) #This Run the Base Class Method
        plus=x+y
        print("The Answer of Stat:",plus)
        #super().add(11,10)

s=Stat() #Create the Object of Derived Class
s.add(2,3) #Run the Derived Class and Base Class Method




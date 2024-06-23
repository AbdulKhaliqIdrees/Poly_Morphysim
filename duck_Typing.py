#Duck Typing
class Duck(object):
    def swim(self):
        print("Fast Swimming in the water")
class Cat(object):
    def swim(self):
        print("Swim like a Duck")
class Crow(object):
    def fly(self):
        print("Fast Flying in the Air")

def show(a):
    a.swim()

d=Duck() #Object of Duck class
show(d)  #Run Function By passing object of Duck Class
print()
c=Cat()  #Object of Cat class
show(c)  #Run Function By passing object of Duck Class
print()
#b=Crow() 
#show(b) #This Create Error and This Error Can be Fixed with the Help of Strong Typing



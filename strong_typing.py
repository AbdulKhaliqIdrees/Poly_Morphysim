#Strong Typing
class Duck(object):
    def swim(self):
        print("Fast Swimming in the water")
class Cat(object):
    def swim(self):
        print("Swim like a Duck")
class Crow(object):
    def fly(self):
        print("Fast Flying in the Air")
class Horse(object):
    def run(self):
        print("Fast Running on the Earth")

def show(a):
    if hasattr(a,"swim"):
        a.swim()
    elif hasattr(a,'fly'):
        a.fly()
    else:
        a.run()
    

d=Duck() #Object of Duck class
show(d)  #Run Function By passing object of Duck Class
print()
c=Cat()  #Object of Cat class
show(c)  #Run Function By passing object of Duck Class
print()
b=Crow() #Object of Crow class
show(b)  #Run Function By passing object of Crow Class
print() 
h=Horse() #Object of Horse class 
show(h)   #Run Function By passing object of Horse Class



#Operator Overloading
class A(object):
    def __init__(self,a):
        self.x=a
    def __add__(self,other): #Define Function To Add objects
        sum=self.x+other.y
        return sum
    
class B:
    def __init__(self,b):
        self.y=b
    
a=A(100) #Create Object of Class A
b=B(200) #Create Object of Class B
print("The Sum of Objects is:",a+b) #Add Two Objects

#print(int.__add__(12,12)) #Define Function To Add Integers 
#print(str.__add__("Ali","Ahmad")) #Define Function To Add Strings
#print(float.__add__(1.2,1.2)) #Define Function To Add Float Integers
#A.__add__(self,other) #Define Function To Add objects

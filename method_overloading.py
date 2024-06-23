#Method Overloading 
'''
class A(object):
    def show(self):
        print("Give the Value of A:")   #No Work
    def show(self,a):
        print("Give the Value of A:",a) #Work 

a=A()
a.show(12)
#This is not a Good Example of Method OverLoading Because First Method is Replaced By Second Method
'''
class Math(object):
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            print("Provide at least two arguments")
        print("The Answer is:",s)

m=Math() #Create Object of Math Class
m.sum(11,12) #Run Method By Passing Two Arguments
print()
m.sum(1,2,3) #Run Method By Passing Three Arguments
#print()
#m.sum() #Run Method By Passing 1 Arguments ##This Give Error
#print()
#m.sum() #Run Method By Passing No Arguments ##This Give  Error
import cmath
a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
d=(b*b-4*a*c)
root1= -b+cmath.sqrt(d)/2*a
root2= -b-cmath.sqrt(d)/2*a
print(root1,root2)
import math
class Calculate:
    s=0
    def perimeter(self,s1=None,s2=None,s3=None):
        if s1!=None and s2!=None and s3!=None:
            s=s1 + s2 + s3
        elif s1!=None and s2!=None:
            s=2 * (s1 + s2)
        else:
            s=2 * math.pi * s1
        return s
    a=0
    def area(self,s1=None,s2=None,s3=None):
        if s1 != None and s2 != None and s3 != None:
            a =  ((1 / 2) * s1 * s2)
        elif s1 != None and s2 != None:
            a =s1 * s2
        else:
            a = math.pi * s1 * s1
        return a
s1 = int(input("enter side:"))
s2 = int(input("enter side:"))
s3 = int(input("enter side:"))
d = Calculate()
print(d.perimeter(s1))
print(d.perimeter(s1, s2))
print(d.perimeter(s1, s2, s3))
print(d.area(s1))
print(d.area(s1, s2))
print(d.area(s1, s2, s3))
n=int(input("enter the number"))
n1=0
n2=1
count=0
if n<=0:
   print("Invalid")
elif n==1:
   print(n1)
else:
   while count < n:
       print(n1)
       num = n1 + n2
       n1 = n2
       n2 = num
       count=count+1
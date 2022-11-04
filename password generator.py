import random as rnd
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="!@#$%^&*()~"
d="1234567890"
a=""
n=int(input("Enter length of password!"))
for j in range(0,n):
    i=rnd.randint(0,2)
    if i==0:
        y=rnd.randint(0,len(s)-1)
        a=a+s[y]
    elif i==1:
        y=rnd.randint(0,len(c)-1)
        a=a+c[y]
    else:
        y=rnd.randint(0,len(d)-1)
        a=a+d[y]
print(a)

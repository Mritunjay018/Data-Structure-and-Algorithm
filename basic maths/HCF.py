n=int(input("enter the first number"))
m=int(input("enter the second number"))
h=min(n,m)
for i in range(1,h):
    if n%i==0 and m%i==0:
        hcf=i
print(hcf)        
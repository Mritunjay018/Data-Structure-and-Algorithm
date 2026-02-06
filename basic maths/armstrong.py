n=int(input("enter the number"))
num=n
sum=0
while n >0:
    
    digit = n % 10         
    sum= sum+ (digit*digit*digit)   
    n = n// 10  
if num==sum:
        print("armstrong number")
else:
        print("not armstrong")    



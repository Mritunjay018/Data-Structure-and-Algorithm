num = int(input("Enter a number: "))
n=num

rev = 0

while num > 0:
    digit = num % 10         # get last digit
    rev = rev * 10 + digit   # add digit to reverse
    num = num // 10          # remove last digit
if rev==n:
     print("palidram number ")
else:
     print("not a palindram")    

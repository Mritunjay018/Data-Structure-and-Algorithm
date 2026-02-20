arr = list(map(int,input("enter the list element ").split()))
freq = {}

for num in (arr):
    freq[num]=freq.get(num,0)+1

result = 0
for num,count in freq.items():
    if count > 1:
        result = result+num
print("sum of repeted elemet are ",result)
print(freq)

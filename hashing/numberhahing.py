n = int(input("enter size of array: "))

# input array
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

# frequency array (0–12)
freq = [0] * 13
for i in range(n):
    freq[arr[i]] += 1

# take all queries first and store them
q = int(input("enter number of queries: "))
queries = [0] * q

for i in range(q):
    queries[i] = int(input())

# now print all answers at once
for j in queries:
    print("count",freq[j])

n = int(input("enter number of n"))
for i in range (0,n):
    for j in range(0,n):
        if i >= j:
            print(j,end=" ")
    print(" ")

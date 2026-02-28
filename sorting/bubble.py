def bubble(arr1):
    n= len(arr1)
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                swap = True
        if not swap:
            break

arr1=[4,5,1,3,2]
bubble(arr1)
print("sorted array is ",arr1)

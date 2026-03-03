def insertion_recursive(arr,n):
    if n==1:
        return
    insertion_recursive(arr,n-1)#recusion first n-1 elements
    current=arr[n-1]
    prev=n-2
    while prev>=0 and arr[prev]>current:
        arr[prev+1]=arr[prev]
        prev -= 1
    arr[prev+1]=current
arr=[5,6,4,2,8]
insertion_recursive(arr,len(arr))
print(arr)


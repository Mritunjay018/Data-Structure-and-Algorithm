def bubble_recursive(array,n):
     
    if n==1:
        return
    for i in range(n-1):
        if array[i]>array[i+1]:
         array[i],array[i+1]=array[i+1],array[i]
    bubble_recursive(array,n-1)#recusrsion call
array = [4,5,1,3,2]
bubble_recursive(array,len(array))
print(array)


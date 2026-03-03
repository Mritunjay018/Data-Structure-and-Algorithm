def insertion(array):
    n= len(array)
    for i in range (1,n):
        current=array[i]#stored value
        prev = i-1
        while prev>= 0 and array[prev]>current:
            array[prev+1]= array[prev]#shift
            prev -= 1
        array[prev+1]= current #insert at current position 
array=[4,6,2,8,1,3,2]
insertion(array)
print(f"array sorted{array} ")
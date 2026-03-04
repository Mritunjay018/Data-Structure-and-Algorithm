def mergesort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    halfleft = array[0:mid]
    halfright= array[mid:]
    halfleft=mergesort(halfleft)#recursive function 
    halfright=mergesort(halfright)#recusciev function 
    return merge(halfleft,halfright)

def merge(left,right):
    temp=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i = i+1
        else:
            temp.append(right[j])
            j=j+1
    temp.extend(left[i:])
    temp.extend(right[j:])
    return temp

array=[6,4,5,8,7,9]
array = mergesort(array)
print(array)

def two_sum(arr, target):
    s = set()
    for num in arr:
        compliment = target - num
        if compliment in s:
            return True
        s.add(num)
    return False

arr = [2, 5, 6, 4, 8, 9]
print(two_sum(arr, 12))

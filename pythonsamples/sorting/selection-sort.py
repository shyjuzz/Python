from random import randint

ARRAY_LENGTH = 10000
# arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

arr = [7,8,5,2,4,6,3]

n = len(arr)

for i in range(n):
    ele = arr[i]
    j = i - 1
    while j >= 0 and ele < arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = ele

print(arr)

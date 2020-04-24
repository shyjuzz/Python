# arr = list(map(int,'5 1 4 2 8'.split()))
from random import randint

ARRAY_LENGTH = 10000
arr = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

for i in range(len(arr)):
    sorted = True
    for j in range(i,len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1], arr[j]
            sorted = False
    if sorted:
        break

print(arr)


def binarySearch(arr, l, r, x):
    while l<= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 400

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")

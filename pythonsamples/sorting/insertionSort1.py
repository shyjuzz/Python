def insertionSort1(n, arr):
    for i in range(1, n):
        j = i-1
        ele = arr[i]
        insert = False
        while j >= 0 and ele < arr[j]:
            arr[j+1] = arr[j]
            insert = True
            print(' '.join([str(i) for i in arr]))
            j -= 1
        arr[j+1] = ele
        if insert:
            print(' '.join([str(i) for i in arr]))



insertionSort1(5,[2,4,6,8,3])

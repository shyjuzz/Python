def countSwaps(a):
    swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                swaps += 1
                a[j] , a[j+1] = a[j+1], a[j]
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")

countSwaps([3,2,1])

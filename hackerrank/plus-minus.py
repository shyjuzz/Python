def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for num in arr:
        if num ==0:
            zero+=1
        elif num > 0:
            pos+=1
        else:
            neg+=1
    print('%.6f'%round(pos/n,6))
    print('%.6f'%round(neg/n,6))
    print('%.6f'%round(zero/n,6))


plusMinus([-4 ,3 ,-9 ,0 ,4 ,1])

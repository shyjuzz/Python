def average(array):
    uni = set(array)
    return sum(uni)/len(uni)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

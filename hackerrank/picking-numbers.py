import itertools

def findsubsets(S,m):
    return list(itertools.combinations(S, m))

# def pickingNumbers(a):
#     max_len = 0
#     p_set = findsubsets(a,2)
#     for t in p_set:
#         diff = [abs(j-i) for i, j in zip(t[:-1], t[1:])]
#         if all(x <= 1 for x in diff):# and len(t) > max_len:
#             print(t)
#     return max_len

def pickingNumbers(a):
    n = len(a)
    a.sort()
    count =[]
    for i in range(n):
        arr=[a[i]]
        for j in range(i+1,n):
            if abs(a[i]-a[j]) == 0 or abs(a[i]-a[j])==1:
                arr.append(a[j])
        count.append( len(arr))
    count.sort()
    return count[len(count) - 1]

a = list(map(int, '4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4'.rstrip().split()))
result = pickingNumbers(a)
print(result)

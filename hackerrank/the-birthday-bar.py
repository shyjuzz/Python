def birthday(s, d, m):
    count = 0
    for i in range( len(s)):
        arr = s[i:i+m]
        if len(arr) == m and sum(arr) == d:
            count+=1
    return count

result = birthday([1, 2, 1, 3, 2], 3, 2)
print(result)

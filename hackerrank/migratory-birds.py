from collections import Counter

def migratoryBirds(arr):
    counter = Counter(arr)
    max_count = -1
    for item in counter:
        if counter[item] > max_count:
            max_count = counter[item]
            min_id = item
        elif counter[item] == max_count and item < min_id:
            min_id = item
    return min_id

s='1 2 3 4 5 4 3 2 1 3 4'
arr = list(map(int, s.rstrip().split()))
result = migratoryBirds(arr)
print(result)

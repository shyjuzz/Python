def compareTriplets(a, b):
    bob = 0
    alice = 0
    for i in range(3):
        print(a[i], b[i])
        if a[i] > b [i]:
            alice += 1
        elif a[i] < b [i]:
            bob += 1
    return [alice,bob]

a= [5 ,6 ,7]
b=[3 ,6 ,10]
print(compareTriplets(a,b))

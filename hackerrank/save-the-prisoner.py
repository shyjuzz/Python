#Terminated due to timeout :(
# def saveThePrisoner(n, m, s):
#     i = s
#     while True:
#         m-=1
#         if m <= 0:
#             break
#         i += 1
#         if i > n:
#             i=1
#     return i

def saveThePrisoner(n, m, s):
    a = s+m-1
    if a > n:
        if a %n ==0:
            return n
        return a%n
    return a
results = []
with open('input00.txt') as f:
    for line in f:
        n, m, s = [int(x) for x in line.split()]
        result = saveThePrisoner(n, m, s)
        results.append(result)
# result = saveThePrisoner(7, 19, 7)
# print(result)

with open('output00.txt') as f:
    i = 0
    for line in f:
        if results[i] != int(line):
            print(i+1,'-',line)
        i+=1

from collections import OrderedDict
n = int(input())
od = OrderedDict()
for i in range(n):
    ip = input()
    if ip in od:
        od[ip] = od[ip] + 1
    else:
        od[ip] = 1
print(len(od))
print(" ".join(str(value) for key, value in od.items()))

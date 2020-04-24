from collections import Counter
no_of_sizes = int(input())
size_list = [int(elem) for elem in input().split()]
dic = Counter(size_list)
number_of_customers = int(input())
total = 0
for index in range(number_of_customers):
    size, price = map(int, input().split())
    if size in dic and dic[size] > 0:
        total += price
        dic[size] = dic[size] - 1
print(total)

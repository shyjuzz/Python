# import array
# arr = [1, 2, 3, 4, 5, 6, 7]
# d = 4
# for i in range(0,d):
#     arr.append(arr.pop(0))
# print(arr)
# arr = [7, 1, 2, 3, 4, 5, 6]
# sorted = sorted(arr)
# len = len(sorted)
# op=[]
# for i in range(0,int(len/2)):
#     # print(len-1-i,',',i)
#     op.append(sorted[len-1-i])
#     op.append(sorted[i])
# if len %2 != 0:
#     op.append(sorted[int(len/2)])
# print(op)


# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# print("{0:.2f}".format(sum(student_marks[query_name])/3))
# N = int(input())
# list = []
# for _ in range(N):
#     splitted = input().split()
#     op = splitted[0]
#     if op == 'insert':
#         list.insert(int(splitted[1]),int(splitted[2]))
#     elif op == 'print':
#         print(list)
#     elif op == 'remove':
#         list.remove(int(splitted[1]))
#     elif op == 'append':
#         list.append(int(splitted[1]))
#     elif op == 'sort':
#         list.sort()
#         print('Sorted ',list)
#     elif op == 'pop':
#         list.pop()
#     elif op == 'reverse':
#         list.reverse()
#     else:
#         print('not supported')
# n = int(input())
# integer_list = map(int, input().split())
# print(hash(tuple(integer_list)))



#
# def swap_case(s):
#     op = []
#     for i in list(s):
#         if i >= 'A' and i <= 'Z':
#             op.append(i.lower())
#         else:
#             op.append(i.upper())
#     return "".join(op)
#
# ip = 'Www.HackerRank.com'
#
# print(swap_case(ip))

import textwrap
my_wrap = textwrap.TextWrapper(width = 4)
wrap_list = my_wrap.wrap(text='ABCDEFGHIJKLIMNOQRSTUVWXYZ')
# for line in wrap_list:
print("\n".join(wrap_list))

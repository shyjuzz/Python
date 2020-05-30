s='abcdez'
t='abcfgh'
s = list(s)
i = len(s) -1
while i >= 0:
    if s[i] == 'z':
        s[i] = 'a'
    else:
        s[i] = chr(ord(s[i]) + 1)
        break
    i-=1

if ''.join(s) != t:
    print(''.join(s))
else:
    print('-1')

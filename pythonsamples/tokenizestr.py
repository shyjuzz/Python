import re
def tokenize(txt):
    output = []
    tokens = re.split('; |, |\*|\n',txt)#|\s+
    offset = 0
    for token in tokens:
        offset = txt.find(token, offset)
        output.append((token, offset, offset+len(token)))
        offset += len(token)
    return output


s = 'name, account balance, total equity, assets, liabilities, last update date'
print(s.split())
# for token in tokenize(s):
#     print (token)
#     assert token[0]==s[token[1]:token[2]]

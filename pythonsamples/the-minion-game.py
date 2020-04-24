
def count_sub(s, sb):
    results = 0
    sub_len = len(sb)
    for i in range(len(s)):
        if s[i:i+sub_len] == sb:
            results += 1
    return results

def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")
    # res = [string[i: j] for i in range(len(string))
    #       for j in range(i + 1, len(string) + 1)]
    # all_substrings = list(set(res))
    # stu_score = 0
    # kevin_score = 0
    # for sub in all_substrings:
    #     if sub[0] in ['A','E','I','O','U']:
    #         kevin_score += count_sub(string, sub)
    #     else:
    #         stu_score += count_sub(string, sub)
    # if kevin_score == stu_score:
    #     print('Draw')
    # elif kevin_score > stu_score:
    #     print('Kevin ',kevin_score)
    # else:
    #     print('Stuart ',stu_score)

s = input()
minion_game(s)

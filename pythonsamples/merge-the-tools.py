import textwrap

def merge_the_tools(string, k):
    for seq in textwrap.wrap(string, k):
        seen = set()
        print("".join([x for x in seq if x not in seen and not seen.add(x)]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

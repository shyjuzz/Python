
def isMagicSquare( mat) :
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += mat[i][i]

    second_diagonal_sum = 0
    for i in range(3):
        second_diagonal_sum += mat[i][2-i]

    if diagonal_sum != second_diagonal_sum:
        return False

    #rowsum
    for i in range(3):
        row_sum = 0
        for j in range(3):
            row_sum += mat[i][j]
        if row_sum != diagonal_sum:
            return False

    #colsum
    for i in range(3):
        col_sum = 0
        for j in range(3):
            col_sum += mat[j][i]
        if col_sum != diagonal_sum:
            return False

    return True

def formingMagicSquare(s):
    ms = [
        [ [ 8, 1, 6 ], [ 3, 5, 7 ], [ 4, 9, 2 ] ],
        [ [ 6, 1, 8 ], [ 7, 5, 3 ], [ 2, 9, 4 ] ],
        [ [ 4, 9, 2 ], [ 3, 5, 7 ], [ 8, 1, 6 ] ],
        [ [ 2, 9, 4 ], [ 7, 5, 3 ], [ 6, 1, 8 ] ],
        [ [ 8, 3, 4 ], [ 1, 5, 9 ], [ 6, 7, 2 ] ],
        [ [ 4, 3, 8 ], [ 9, 5, 1 ], [ 2, 7, 6 ] ],
        [ [ 6, 7, 2 ], [ 1, 5, 9 ], [ 8, 3, 4 ] ],
        [ [ 2, 7, 6 ], [ 9, 5, 1 ], [ 4, 3, 8 ] ],
    ]
    min = 999999
    for k in range(0, 8):
        sum = 0
        for i in range(0, 3):
            for j in range(0, 3):
                sum += abs(s[i][j] - ms[k][i][j])
        if sum < min:
            min = sum
    print(min)

    # print(isMagicSquare(s))

s=[
[4 ,8, 2],
[4, 5 ,7],
[6 ,1 ,6]
]
result = formingMagicSquare(s)


# Ans = 81
# for P in permutations(range(1,10)):
#     if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
#         Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0,9)))
# print(Ans)

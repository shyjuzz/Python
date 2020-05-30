
def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    for x in apples:
        if x+a >=s and x+a <=t:
            acount+=1
    print(acount)
    ocount = 0
    for x in oranges:
        if x+b >=s and x+b <=t:
            ocount+=1
    print(ocount)

countApplesAndOranges(7, 11, 5, 15, [-2,2,1], [5,-6])

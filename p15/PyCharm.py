
re = 1
def cheng(*num):
    global re
    for i in num :
        re = i * re
    print (re)

cheng(1,2,3,4,5)


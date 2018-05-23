re = 1
i = (1,2,3,4,5)
def fun(*num):
    global re
    while re < 11 :
        re = i*re
    return(re)
fun(re)

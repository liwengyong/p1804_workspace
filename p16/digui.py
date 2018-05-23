
def callnum(a):
    if a >=1:
        result = a*callnum(a-1)
    else:
        result = 1
    return result
s = callnum(997)
print(s)

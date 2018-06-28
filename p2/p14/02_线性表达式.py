
def wai(a,b):
    def nei(x):
        nonlocal a,b   #在使用之前一定不要被使用 包括 print
        print('y = %d * %d + %d'%(a,x,b))
        a += 1
        b += 1
        y = a*x+b
        return y

    return nei

wai(1,2)(3)

w = wai(2,3)
print(w(3))

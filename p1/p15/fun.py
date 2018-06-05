
def fun():
    print('*'*52)
    print(a)
a = 2
fun()

def fun1(a,b,c,d):
    print('*'*52)
    print(a,b,c,d)
a = 1
b = [1,2,3,'a','f']
c = {'a':'s','b':'re'}
d = (12345)
fun1(a,b,c,d)

def fun2(*a):
    print('*'*52)
    print(a)
a = 1
b = [1,2,3,'a','f']
c = {'a':'s','b':'re'}
d = (12345)
fun2(a,b,c,d)

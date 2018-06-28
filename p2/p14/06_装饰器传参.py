def wai(f):
    def nei(name = '员工'):
        name = input('yaan')
        if name == '员工':
            f()
        else:
            print('内部专用')
    return nei

@wai
def f1():
    print('f1')
@wai
def f2():
    print('f2')
def f3():
    print('f3')
def f4():
    print('f4')

f = input('f')
if f == 'f1':
    f = f1
#e = wai(f)
#e('员工')
f2('abcde')

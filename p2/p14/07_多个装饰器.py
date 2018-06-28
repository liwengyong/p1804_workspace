def wai(f):
    def nei(name = '员工'):
        name = input('yaan')
        if name == '员工':
            f()
        else:
            print('内部专用')
    return nei
def wai1(f):
    def nei1(pwd = 123):
        pwd = input('pwd')
        if pwd == '123':
            f()
        else:
            print('内部专用')
    return nei1


@wai
def f1():
    print('f1')
@wai
@wai1
def f2():
    return('f2')
def f3():
    print('f3')
def f4():
    print('f4')

print(f2())
#f = input('f')
#if f == 'f1':
#    f = f1
#e = wai(f)
#e('员工')
#f1()


def test1():
    print('-----test1 01------')
    print(num)
    print('-----test1 02------')

def test2():
    print('-----test2 01------')
    test1()
    print('-----test2 01------')

def test3():
    try:
        print('-------test3 01--------')
        test1()
        print('-------test3 02--------')
    except Exception as r:
        print('程序出现异常，内容是:%s'% r)
    print('-----test3 03--------')

test3()
print('------分割线------')
test2()

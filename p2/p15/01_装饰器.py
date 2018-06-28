#1.无参数
def wai(fun):
    def nei():
        print('检查')
        fun()
    return nei

@wai
def foo():
    print('foo')
foo()
#2.(1)有一个参数
def wai(fun):
    def nei(n):
        print('检查传递的参数是%d'%n)
        print('检查')
        fun(n)
    return nei

@wai
def foo(a):
    print('foo')
    print('参数是%d'%a)
foo(1)
print('*'*52)
#2.(2)有2个参数
def wai(fun):
    def nei(n,l):
        print('检查传递的参数是%d'%n)
        print('检查传递的参数是%d'%l)
        print('检查')
        fun(n,l)
    return nei

@wai
def foo(a,b):
    print('foo')
    print('参数是%d'%a)
    print('参数是%d'%b)
foo(2,5)
print('*'*52)
#3.不定长参数
def wai(fun):
    def nei(*args,**kwargs):
        print('检查传递的参数是',args)
        print('检查传递的参数是',kwargs)
        print('检查')
        fun(*args,**kwargs)
    return nei

@wai
def foo(*args,**kwargs):
    print('foo')
    print('参数是',args)
    print('参数是',kwargs)
foo(2,5,'a', a = 1 ,b = 2 , c = 'a')
print('*'*52)
#4.返回值
def wai(fun):
    def nei():
        print('检查')
        return (fun())
    return nei

@wai
def foo():
    return ('foo')
print(foo())
print('*'*52)
#5.增加外部 参数传递
def jsq(a):   #1.最外层添加 方法
    def wai(fun):  #传递的函数的引用
        def nei():  #传递的 函数所需要的 参数
            print('检查')
            print('判断需要使用参数 这里接受 ',a)
            return (fun())  # 2
        return nei
    return wai  #2.返回 最近的函数
@jsq(12345)   #3.调用最外层的装饰器 名称
def foo():  # 1
    return ('foo')
foo()



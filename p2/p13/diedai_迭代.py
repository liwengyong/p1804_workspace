#coding=utf-8
def fib(day):
    n = 0
    a,b = 0,1
    while n < day:
        yield(b)
        a,b = b,a+b
        n += 1 # 天数递增
    return 'ok'
a = fib(100)
print(next(a))
print(next(a))
print(next(a))

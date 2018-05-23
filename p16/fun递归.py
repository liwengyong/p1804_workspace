'''
def a():
    print('a函数')
def b():
    print('b函数')
    b()
b()
n = 10
def jiecheng(n):
    i = 1
    while n >= 1 :
        i = i*n
        n = n-1
    return(i)

jiecheng(10)
'''
def jiecheng(n):
    s = 0
    if n >=1:
       # n*(n-1)!
        n*jiecheng(n-1)
    else :
        s = 1
    return s
n = jiecheng(3)
print(n)

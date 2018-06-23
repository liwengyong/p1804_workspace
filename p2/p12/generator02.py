'''
def container(start,end):
    while start < end :
        print(start)
        start += 1
'''
from inspect import isgeneratorfunction
def container(start,end):
    while start < end :
        yield start   #用于创建生成器 generator
        start += 1


c = container(0,59999999999999999999999999)
print(isgeneratorfunction(container))
print(type(c))
print(c)
print(next(c))
#next(c)
#for i in c:
#    print(i)

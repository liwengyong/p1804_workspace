

def hanshu(canshu):
    print('*'*52)
    print(canshu)

#hanshu()

a = 1
b = [1,2,3,4,5]
c = 'zhangsan'
hanshu(b)

def hanshu2(*a):
    print('*'*10)
    print(a)
    '''
函数想接收多个参数，可以使用
def 函数名（*型参）
'''
hanshu2(2,2,3,'aa','d')


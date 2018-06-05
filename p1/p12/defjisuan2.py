#coding=utf-8
print('欢迎来到人工智能专属计算器')
def jia (a,b):
    return(a+b)
def jian (a,b):
    return(a-b)
def cheng (a,b):
    return(a*b)
def chu (a,b):
    return(a/b)
while True :
    a = int (input('输入第一个数字'))
    if a == 000 :
        break
    f = 1
    while f <= 3 :
        fuhao = input ('请输入运算符号：（+ - × / ）')
        if fuhao == 'q':
            break
        elif fuhao != '+' and fuhao != '-' and fuhao != '*'and fuhao != '/' and fuhao != 'q':
            print ('输入的内容无法识别，请输入标点符号')
        f = f + 1
        b = int(input('输入下一个数字'))
        if fuhao == '+':
            a = jia (a,b)
        elif fuhao == '-':
            c = jian (a,b)
        elif fuhao == '*':
            c = cheng (a,b)
        else :
            c = chu (a,b)
        print (a)
    print (a)

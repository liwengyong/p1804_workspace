
def systemMenu():
    print('*'*52)

    print ('欢迎使用名片管理系统')
    print ('1.新建名片')
    print ('2.查看名片')
    print ('3.查询名片')
    print ('4.存储功能')
    print('*'*52)

def tuichu():
    print ('exit')
def newCard():
    print ('请输入新的名片')
def sAll():
    print('请输入我也不知道这是啥玩意')
def sOne():
    print('请输入我也不知道这是啥玩意')
def defCard():
    print('请输入def卡')

systemMenu()
while True:
    user = int(input('请输入你希望操作对应的编号'))
    if user == 1 :
        newCard()
    elif user == 2 :
        sAll()
    elif user == 3 :
        sOne()
    elif user == 4 :
        defCard()
    else :
        tuichu()
        break

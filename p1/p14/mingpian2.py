list_card = []
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
    print('*'*52)
    print ('开始创建名片')
    name = input('请输入姓名：')
    com = input ('请输入公司：')
    phone_num = input('请输入电话：')
    dic = {'name':name,'company':com,'phone':phone_num}
    list_card.append(dic)
    print('名片保存成功!姓名是：%s'% dic['name'],'\n''公司是:%s'% dic['company'],'\n''电话是:%s'% dic['phone'])
    print(list_card)
def sAll():
    sAll = input('请输入要查看的key:')
    for sAll in list_card:
        if sAll == 'name':
            print(list_card)
def sOne():
    print('请输入要查看的名片:')
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
new_Card()

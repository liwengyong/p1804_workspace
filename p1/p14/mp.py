
list_card = []
def systemMenu():
    print('*'*52)
    print('欢迎使用名片管理系统')
    print('1.新建名片')
    print('2.查找名片')
    print('3.显示名片')
    print('4.修改名片')
    print('5.删除名片')
    print('6.退出系统')
    print('*'*52)

def newCard():
    print('开始创建名片')
    name = input('请输入名字:')
    com = input('请输入公司:')
    phone_num = input('请输入电话:')
    dic = {'name':name,'company':com,'phone':phone_num}
    global list_card
    list_card.append(dic)
    print('名片保存成功!姓名是：%s'% dic['name'],'\n''公司是:%s'% dic['company'],'\n''电话是:%s'%dic['phone'])
    print(list_card)

def sAll():
    global list_cad
    f_name = input('请输入要查找的姓名:')
    find = 0
    for i in list_card:
        if f_name == i['name']:
            print('姓名是:%s\n公司是:%s\n电话是:%s'%(i['name'],i['company'],i['phone']))
            find = 1
            break
        if find == 0 :
            print('不能找到这个人')

def sOne():
    global list_card

    for i in list_card:
        print('姓名是:%s\n公司是:%s\n电话是:%s'%(i['name'],i['company'],i['phone']))
    print('----------显示完毕----------')

def defCard():
    global list_card
    ch = input('请输入需要修改的名字:')
    for i in list_card :
        if i['name'] ==ch :
            i['name'] = input('请输入新的名字:')
            i['cpmpany'] = input('请输入新的公司:')
            i['phone'] = input('请输入新的电话:')
            print('----------修改完毕----------')
            return
    print('----------查无此人----------')

def delCard():
    global list_card
    de = input('请输入要删除的姓名')
    for i in list_card :
        if i['name'] == de:
            list_card.remove(i)
            break
    print('----------删除完毕----------')

def main():
    systemMenu()

    while True:
        user =input('请输入你希望操作对应的编号:')
        if user =='1':
            newCard()
        elif user == '2':
            sAll()
        elif user == '3':
            sOne()
        elif user == '4':
            defCard()
        elif user == '5':
            delCard()
        elif user == '6':
            break
        else :
            print('输入有误，请重新输入')
main()


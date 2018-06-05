#今天要写的是一个简单的医院挂号系统，你是挂号管理员
#这两行不参与循环，所以放在外边
print('*='*25)
print('尊敬的挂号管理员您好,欢迎您再次使用本系统')
list_guahao = []#定义一个列表，用来存放数据
def menu ():#这是菜单
    print('1.录入病人信息')
    print('2.显示录入列表')
    print('3.查找病人房房号')
    print('4.修改录入信息')
    print('5.删除病人信息')
    print('6.退出挂号系统')
    print('×='*25)

def luru():#这是需要录入的信息
    print('开始录入信息')
    name = input('请输入名字')
    sex = input('请输入性别')
    fanghao = input('请输入病房号')
    dic = {'name':name,'sex':sex,'fanghao':fanghao}
    list_guahao.append(dic)#建立一个字典，用来存放数据，将字典追加到列表中
    #print('信息录入成功！姓名是:%s\n性别是%s\n病房号是%s\n'%(dic['name'],dic['sex'],dic['fanghao']))
    print('姓名是:%s\n性别是:%s\n房号是:%s\n'%(dic['name'],dic['sex'],dic['fanghao']))
    print(list_guahao)#然后显示一下列表
    print('显示完毕'.center(25,'*'))

def xianshi():#显示录入信息
    for i in list_guahao:
        print('姓名是:%s\n性别是:%s\n病房号是:%s\n'%(i['name'],i['sex'],i['fanghao']))
    if len(list_guahao) == 0:
        print('没有任何名片记录')

def find():
    print('前台的小姐姐打来电话:有家属要来探病，想问一下他住在几号病房？')
    f = input('请输入要查找的姓名:')
    fin = 0#默认表示没有找到
    for i in list_guahao:
        if f == i['name']:
            print('病人住在%s号'%i['fanghao'])
            fin = 1
            bireak
    if fin == 0:
        print('找不到这个人，你问一下家属确定是这个医院吗？')


def gai():
    #修改函数
    print('在整理录入信息中发现信息与前台登记不符需要进行修改')
    ch = input('请输入需要修改信息的病人')
    for i in list_guahao:
        if i['name'] == ch :
            i['name'] = input('请输入新的名字')
            i['sex'] = input('请输入病人的性别')
            i['fanghao'] = input('请输入病房号')
            print('修改完毕'.center(25,'*'))
            return
    print('查无此人'.center(25,'×'))

def deln():#删除函数
    print('信息录入系统需要每隔三个月进行一次整理，需要删除已出院并且复查完毕的病人信息')
    de = input('请输入要删除的病人姓名')
    for i in list_guahao:
        if i['name'] == de :
            list_guahao.remove(i)
            break
    print('删除完毕'.center(25,'*'))



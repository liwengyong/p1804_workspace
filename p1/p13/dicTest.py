
dic = {'name':'zhangsan',
        'age':18,
        'sex':'nan',
        'phone':125}
dic2 = {'name':'zhangsan',
        'age':18,
        'phone':125}
dic['name'] = '李'
dic['eamil'] = ['1232qq.com']
print(dic)
print(dic['name'])

com = input ('请输入公司：')
dic['com'] = com
print(dic)

list_mingpian = []
list_mingpian.append(dic)
list_mingpian.append(dic2)
print(list_mingpian)

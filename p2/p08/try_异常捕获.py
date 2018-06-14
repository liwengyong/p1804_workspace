
try:   #希望 抓获 哪一部分代码，可能出现的异常
    print(1)
    phone_number = input('请输入手机号码')
    print(int(phone_number))
    #open('a.txt','r')
    #print('%d'%'name')
    #print(name)
    print('张瑞芸')
    print(True)
except Exception as error_result:   #当出现了指定异常，我们希望执行的操作
    print('程序出现了问题 %s'% error_result)
else:
    print('程序没有任何异常')

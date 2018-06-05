import xm,time,fz
while True:
    xm.menu()
    #获取用户输出
    user = input('请选择你要进行的操作编号:')
    if user == '1':
        xm.luru()
    elif user == '2':
        xm.xianshi()
        print('显示完毕'.center(25,'x'))
    elif user == '3':
        xm.find()
    elif user == '4':
        xm.gai()
    elif user == '5':
        xm.deln()
    elif user == '520':
        print(fz.mv())
    elif user == '521':
        print(fz.mn())
    elif user == '522':
        print(fz.tz())
    elif user == '525':
        print(fz.zet())
    elif user == '666':
        print(fz.my())
    elif user == '滚':
        print(fz.zuji())
    elif user == '6':
        #print(time.asctime())
        print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print('感谢您的使用,晚安，再见。')
        break
    else:
        print('输入有误，请重新输入')


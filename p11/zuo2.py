
ia = '123'
ip = '321'
i = 0
while True :
    aa = input ('请输入帐号：')
    ap = input ('请输入密码：')
    if aa == ia and ap == ip:
        a = int (input('$欢迎来到我的世界$'))
    else :
        i = i + 1
        print ('error%dci'%i)
        break
        if i == 4:
            print ('您已经连续输错4次了，请重新登录')
            break

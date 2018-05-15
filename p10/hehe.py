while True :
    import random

    me = int(input('请出小拳拳:'))

    pc = random.randint(1,3)
    while me >=4 :
        me = int(input('您输入的数据有误，请重新输入:') )
    if pc == 1 :
        print('电脑出的是石头')
    elif pc == 2 :
        print('电脑出的是剪刀')
    else :
        print('电脑出的是布')
    if ((me == 1 and pc == 2) or (me == 2 and pc == 3) or (me ==3 and pc == 1)):
        print('win!!!')
    elif me == pc:
        print('draw!!!')
    elif me > 3 :
        print('数据异常 请输入1 2 3 之间的数字')
    else :
        print('lose!!!')

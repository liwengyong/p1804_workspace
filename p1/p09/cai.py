userInput = 'begin'
while userInput == 'begin':
    import random
    shitou = '石头'
    jiandao = '剪刀'
    bu = '布'

    me = input('请出小拳拳:')
    if me == 'q':
        userInput = 'q'
    pc = random.randint(1,3)
#    while me >= 4 :
#        me = input('您输入的数据有误，请重新输入:')
    if pc == 1 :
        pc = shitou
        print('电脑出的是石头')
    elif pc == 2 :
        pc = jiandao
        print('电脑出的是剪刀')
    else :
        pc = bu
        print('电脑出的是布')
    if (me == shitou and pc == jiandao) or (me == jiandao and pc == bu) or (me ==bu and pc == shitou):
        print('win!!!')
    elif me == pc:
        print('draw!!!')
#    elif me > 3 :
#        print('数据异常 请输入1 2 3 之间的数字')
    else :
        print('lose!!!')

import random

me = input('请出招:')

a='石头'
b='剪刀'
c='布'

pc = random.randint(1,3)
#print ('电脑出拳: %d '% pc )

if pc and me == 1 :
    print ('石头')
elif pc and me == 2 :
    print ('剪刀')
else :
    print('布')

if ((me == a and pc == b) or (me == b and pc == c) or (me ==c and pc == a)):
    print('win')
elif me == pc :
    print('draw')
else :
    print('lose')

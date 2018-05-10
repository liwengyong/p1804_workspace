import random

me = int(input('请出拳王石头（1）/ 剪刀（2）/布（3）:'))

石头 = 1
剪刀 = 2
布 = 3

pc = random.randint(1,3)
print ('电脑出拳: %d '% pc )

if pc and me == 1 :
    print ('石头')
elif pc and me == 2 :
    print ('剪刀')
else :
    print('布')

if ((me == 1 and pc == 2) or (me == 2 and pc == 3) or (me ==3 and pc == 1)):
    print('win')
elif me == pc :
    print('draw')
elif me > 3 :
    print('数据异常 请输入1 2 3 之间的数字')
else :
    print('lose')

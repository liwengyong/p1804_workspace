
import random
a = random.randint(1,100)
i = 0
for i in range(1,11):
    b = int (input('请输入数字：'))
    if a > b :
        print ('猜小了哦')
    elif a < b :
        print ('猜大了哦')
    else :
        print ('猜中了哦')
        break
    i = i + 1

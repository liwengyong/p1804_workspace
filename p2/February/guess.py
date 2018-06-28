from random import randint
n=randint(1,100)
#print('生成随机数为%d' %n)
i=0
while True:
    num=int(input('输入你猜的数字1-100:'))
    i+=1
    if(num>n):
        print('错误，数字太大了!')
    elif(num<n):
        print('错误，数字太小了!')
    else :
        print('回答正确')
        break
print('一共猜了 %d 次。' %i)
if i<=5:
    print('你太聪明了，这么快猜了出来！')
else:
    print('还需要改进方法，以便更快才出来！')


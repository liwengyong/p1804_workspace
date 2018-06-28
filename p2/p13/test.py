
list = []
fiblist = []
for i in range(100):   #得到100数列
    list.append(i)
list = iter(list)
n = 0
a,b = 0,1
while n < 100:   #得到斐波那契数列
    fiblist.append(b)
    a,b = b,a+b
    n += 1
for i in list:   #判断输出 满足的 数列
    if i in fiblist:
        print(i)

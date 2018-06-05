
t = ()
t1 = ('zhangsan',22,'男')
t2 = ('张三丰',)
t5 = ('鲧',20,'nv')
print(t2)
print(type(t2))
print(t5)
print(t1[2])
print(t1.index(22))
print('姓名是：%s\n年龄是: %d\n性别是：%s'% t1 )
print('姓名是：%s\n年龄是: %d\n性别是：%s'% t5 )

for i in t1:
    print(i)
for i in t5:
    print(i)
print(t5[2])
print(t5.index('nv'))

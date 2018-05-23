list_name = []
while True:
    n = input('请输入同学姓名：')
    list_name.append(n)
    if n  == 'q' :
        break
print (list_name)
print('第 3 位是:%s '% list_name[3])
print('第 5 位是:%s '% list_name[5])
print('第 8 位是:%s '% list_name[8])
print('第 10 位是:%s '% list_name[10])
list_name.sort()
print(list_name)
list_name.sort(reverse=True)
print(list_name)
print(list_name.pop())
del list_name[8]
print(list_name)
l = [1,2,3,4,5,6,7]
print(list_name.extend(l))
print(list_name)
print('小明所在的位置是 %d'% list_name.index('鲧'))

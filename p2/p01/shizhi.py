
f = open('shi.txt','wb+')
a = f.readline()
b = f.tell()
print('第一行內容:%s'%a)
print('當前位置是:%d'%b)
a = f.readline()
b = f.tell()
print('第2行內容:%s'%a)
print('當前位置是:%d'%b)
c = f.seek(0,0)
print(f.readline())
f.close()
'''
print(a,b,c)
f1 = open('shi.txt','w')
for i in a :
    f1.write()
'''

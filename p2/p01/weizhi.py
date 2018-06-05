
f = open('shi.txt','rb')
n = f.read(5)
f.read(2)
f.seek(2,1)
print('前五個內容是:%s'%n)
position = f.tell()
print('當前位置是:%d'%position)
f.close()

'''
f = open('test.txt','r')
st = f.read(30)
print('数据是：',st)

position = f.tell()
print('当前位置:',position)

f.seek(5,0)

position = f.tell()
print('当前位置:',position)

f.close()
'''
f = open('test.txt','rb+')

position = f.tell()
print('当前位置',position)

f.seek(-3,2)

st = f.read()
print('读取的数据:',st)

f.close()

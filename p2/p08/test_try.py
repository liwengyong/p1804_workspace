
n = input('请输入文件名')
l = open(n,'r')
try:
    z = l.read()
    print(z)
except Exception as r:
    print(r)
finally:
    l.close()
print(l.closed())
#else:
 #   print('程序没有任何问题')
print('------------------')


f = open('shi.txt','w')
f.write('煮豆燃豆萁，\n')
f.write('萁在釜下泣。\n')
f.write('我烬你熟了，\n')
f.write('正好办教席。\n')
f.close()

f = open('shi.txt','r')
n = f.readlines()

g = open('shi.txt','w')
for i in n :
    s = i[:len(i)-1]
    g.write(s+'$\n')

f.close()
g.close()

f1 = open('shi.txt','r')
a = f1.read()
print(a)
f1.close()

print('文件的名字是:%s'% f1.name)
print('文件是否已经关闭:%s'% f1.closed)
print('该文件的打开模式是:%s'% f1.mode)

f = open('kk.jpg','rb')
cimg = f.read()
print(cimg)
f.close()


f = open('1.txt','wb')
f.read(a)
f.close()

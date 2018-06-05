
f = open('shi.txt','w')
content = f.write('煮豆燃豆萁，\n')
content = f.write('萁在釜下泣。\n')
content = f.write('我烬你熟了，\n')
content = f.write('正好办教席。\n')
f.close()

f = open('shi.tx','r')
n = f.read()
print(n)
f.close()

f = open('shi.txt','a')
f.write('*_*')
f.close()

f =  open('shi.txt','r')
c = f.read()
print(c)
f.close()

f = open('shi.txt','a')
f.write(c)
f.close()

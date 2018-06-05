
a = input('請輸入要復制的文件名:')
b = open(a,'r')
f = a.rfind('.')
e = a[:f]+'[復件]'+a[f:]
e = '[復件]'+a
#c = open('new.txt','w')
c = open(e,'w')
while True :
    d = b.read(1024)
    if len(d) == 0 :
        break
    c.write(d)
b.close()
c.close()



f = open('2.txt','w')
f.write('大风起兮云飞扬\n')
f.write('威加海内兮归故乡\n')
f.write('安得猛士兮守四方\n')

f = open('2.txt','r')
n = f.readlines()
l = open('2.txt','w')
for i in n :
    z = i[:len(i)-1]
    l.write(z+'*_*\n')
f.close()
l.close()

f = open('2.txt','r+')
l = f.readlines()
y = open('2.txt','a+')
for t in l :
    z = t[:len(t)-1]
    y.write(z+'|\n')
f.close()
y.close()


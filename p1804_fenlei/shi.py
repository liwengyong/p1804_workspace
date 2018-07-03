
a = 0
for b in range(1,5):
    for c in range(1,5):
        for d in range(1,5):
            if b!=c and c!=d and d!=b:
                a+=1
                print('输出的第%d个三位数是%d%d%d'%(a,b,c,d))

print('*'*52)

list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in list :
    for k,v in i.items():
        for j,u in v.items():
            print(k,j,u)

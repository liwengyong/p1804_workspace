list=[{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"},'成都':{'面积':'16平米','人口':'50万'}}]


for i in list:
    for k,v in i.items():
        for j,l in v.items() :
            print(k,j,l)
'''
list=[{{"面积":"1000平","人口":"200w"}:"北京",{"面积":"600平","人口":"150w"}:"上海"}]

for i in list :
    for a,b in i.items():
        for c,d in k.items():
            print(b,c,d)
'''

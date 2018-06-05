
dic = {'a':1,'b':2,'c':3,'d':4,'e':5}
k_dic = dic.keys()
v_dic = dic.values()
kv_dic = dic.items()
print(k_dic)
print(dic.keys())
print(v_dic)
print(dic.values())
print(kv_dic)
print(dic.items())
'''
for i in dic :
    for k in dic.keys():
        for v in dic.values():
            print(k,v)
'''
tup = ('name','zhangsan')
print(type(dic.items()))
for k,v in dic.items():
    print('k=',k)
    print('v=',v)


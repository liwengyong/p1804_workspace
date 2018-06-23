#encoding=utf-8
'''
a = [1,2,3]
b = [i for i in range(1,10)]
c = [s for s in 'hello world']
d = [i for i in range(1,10,2)]
print(a)
print(b)
print(c)
print(d)
b = (i for i in range(1,10))
print(a)
print(b)
'''
a = [i for i in range(1,10) if i % 2 == 0 ]
s = [(i,j)for i in range(1,10) for j in range(1,3)]
b = [i for i in range(1,5) for j in range(3)]
c = [j for i in range(1,5) for j in range(3)]
print(b)
print(c)

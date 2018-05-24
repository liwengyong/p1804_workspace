'''
def add(a,b):
    print(a+b)

print(add(1,2))

a = lambda a,b : a+b
b = lambda x,y : x-y
c = lambda c,d : c*d
d = lambda w,z : w/z
print(c(5,2))
'''

l = [(lambda x,y:x**y),(lambda a,b,c:a+b+c),(lambda s,d=2:s+d)]
print(l[0](2,4),l[1](2,4,5),l[2](5))

d = {'a':(lambda:2+3),'b':(lambda:2*3),'c':(lambda:2**3)}
print(d['a'](),d['b'](),d['c']())




L = [x*2 for x in range(5)]
print(L)
L = ( x*2 for x in range(5))
print(L)
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))
for i in L:
    print(i)

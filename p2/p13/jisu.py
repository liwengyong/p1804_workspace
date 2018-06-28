
def jishu():
    while a < 100:
        if a % 2 != 0 :
            b = yield a
            a += 1
f = jishu()
print(f)

l = [i for i in range(1,101) if i %2 != 0 ]

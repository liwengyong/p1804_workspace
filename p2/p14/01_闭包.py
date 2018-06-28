
def wai(start=0):
    def nei():
        nonlocal start   #说明要访问的变量是外部变量
        start += 1
        print(start)
        return ' '
    return nei

a = wai(1)
a()
a()
a()
b = wai(1)
b()


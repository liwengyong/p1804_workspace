list_nn  = ['liwenyong',21,'nan']
a = 25
def test1():
    global a
    a +=1
    print(a)
    list_nn.extend('0350')
    print(list_nn)
def test2():
    print(a)

test1()

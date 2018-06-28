
def wai(fun):
    def nei():
        print('正在验证')
        fun()
    return nei

@wai
def Test():
    print('哈哈')

Test()

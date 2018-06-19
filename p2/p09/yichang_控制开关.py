
class Test(object):
    def __init__(self):
        self.switch = 'open'
    def div(self,a,b):
        try:
            return a/b
        except Exception as ret:
            if self.switch == 'open':
                print('出现了异常:%s'%ret)
            else:
                raise
t = Test()
t.switch = 'close'
print(t.div(2,0))

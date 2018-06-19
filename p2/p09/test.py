
a = '12345'
b = 'qwer'

class HuError(Exception):
    def __init__(self,hu_error):
        self.name = hu_error

class PwdError(Exception):
    def __init__(self,pwd_error):
        self.name = pwd_error
def get_hu():
    c = input('请输入用户名')
    d = input('请输入密码')
    if c != a :
        raise HuError('用户名不正确')
    elif d != b:
        raise PwdError('密码错误')

try :
    get_hu()

except Exception as ln:
    print('遇到了异常,内容是%s'%ln)

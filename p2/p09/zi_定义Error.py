
class MyError(Exception):
    def __init__(self,str_error):
        self.name = str_error

def get_pwd():
    pwd = input('请您输入密码:')
    if len(pwd) < 6:
        raise MyError('密码小于6位不符合要求！！！')
try:
    get_pwd()
except Exception as re:
    print('遇到了异常:内容是%s'%re)

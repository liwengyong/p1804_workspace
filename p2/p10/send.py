#__all__指定的模块方法，表示from导入后需要引用的方法
__all__ = ['send','sendmsg']
def send():
    print('asdfad')
def sendmsg():
    print('gsdgdsgs')
if __name__ == '__main__':
    print('测试')
    send()
    sendmsg()

#encoding=utf-8

name = input('请输入姓名：')
company = input('请输入公司：')
title = input('请输入职位：')
phone = input('请输入电话：')
email = input('请输入邮箱：')

print('*'*52)
print(company)
print()
print('%s(%s)' % (name,title))
print()
print('电话：%s' % phone)
print('邮箱：%s' % email)
print('*' * 52)

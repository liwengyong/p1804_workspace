
age = int (input('请输入年龄：'))

if age > 1 and age < 10:
    print('幼年')
elif age >11 and age < 20:
    print('青少年')
elif age > 21 and age < 30:
    print('少年')
elif age > 31 and age < 40:
    print('青年')
elif age > 41 and age < 60:
    print('壮年')
elif age > 61 and age < 80:
    print('中老年')
else:
    print('老年')

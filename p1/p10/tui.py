
sex = input('请输入性别：')
age = int(input('请输入年龄：'))

if sex == '男':
    if age <= 60 :
        print ('继续奋斗，多娶媳妇。')
    else:
        print ('>60岁，归隐山林，安详晚年。')
else:
    if age <= 55:
        print ('继续努力，多生孩子，多读书。')
    else:
        print ('>55岁，允许加入广场舞大军。')

a = int(input('请输入年份：'))
while a >= 2000 and a <= 3000:
    if a % 4 == 0 and a % 100 != 0 :
        print ('今年是闰年：')
    elif a % 400 == 0 :
        print ('今年是闰年:')
    else:
        print ('今年是平年：')
    a=a+1
    if a > 3000 :
        print ('输入有误，请输入2000-3000的值:')
    break

while True :
    a = int (input ('今年是：'))
    while a >= 2000 and a <= 3000 :
        if a % 4 == 0 and a % 100 != 0 :
            print ('是闰年')
        elif a % 400 == 0 :
            print ('是闰年')
        else :
            print ('是平年')
        continue
        if a < 2000 and a > 3000 :
            print ('您输入的值有误，请输入2000-3000之间的数字')
        break

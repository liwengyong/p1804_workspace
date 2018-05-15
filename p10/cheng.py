a = 1
while a < 10 :
    b = 1
    while b<=a:
        c = a * b
        print ('%d * %d = %d'%(a,b,c),end ='\t' )
        b = b+1
    a = a+1
    print('\n')

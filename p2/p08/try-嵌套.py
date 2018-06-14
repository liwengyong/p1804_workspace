
try:
    print('name')

    try:
        for i in range(1,10):
            print(i)
    except Exception:
        print('for 循环出了问题')

except Exception as a:
    print(a)

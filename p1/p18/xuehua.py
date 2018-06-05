import random,time
def a(b):
    num = random.randint(1,5)
    snow = random.randint(1,2)
    print(b*num,end=' ')
    print('*×'*snow)
    time.sleep(0.2)
    a(b)

a('\t\t\t')

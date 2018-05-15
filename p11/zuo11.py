
sum = 0
for i in range (1,101):
    print(i)
    if i % 2 == 0 :
        sum = sum + i
        i = i + 2
print ('1到100的偶数和是 %d'% sum)

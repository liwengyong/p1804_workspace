a = 0
for i in range(1,5):
    for j in range(1,5):
        for n in range(1,5):
            if i != j and j != n and n != i :
                print(i*100 + j *10 + n )
                a += 1
print(a)

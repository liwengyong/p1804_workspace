def test(out):
    def test_in(i):
        print(i)
        return i + out
    return test_in
#test_i = test(1)
#test_i (2)
n = test(1)(2)
print(n)

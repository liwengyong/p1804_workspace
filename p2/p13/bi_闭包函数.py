
def funout(out=1):
j()
    outlist = [out]
    def funin():
        outlist[0] += 1
        print(outlist[0])
    return funin

ain = funout()
print(id(ain))
ain()
ain()
cin = funout()
print(id(cin))
cin()

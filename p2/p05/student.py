
class Student:
    def __init__(self,name,sex,age,):
        self.name = name
        self.sex = sex
        self.age = age
        self.dic = {}
    def add_chengji(self,k,v):
        self.dic[k] = v

    def zhuan(n,m):
        for i in range(1,2):
            k = input('科目')
            v = int(input('成绩'))
            n.add_chengji(k,v)

    def __str__(self):
        return self.name+'的性别是'+self.sex+'年龄是'+str(self.age)+'成绩是'+str(self.dic)



zhang = Student('张三','男',20,)
li = Student('李四','女',12)
wang = Student('王五','男',16)

zhang.zhuan('张三')


f=open('aa.txt','w')
print(zhang)
f.write(zhang.__str__())
f.write(li.__str__())
f.write(wang.__str__())
f.close()

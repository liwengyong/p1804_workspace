print('欢迎使用某某学院学生管理系统')

def menu():
    print('1.')
    print('2.')
    print('3.')
    print('4.')
    print('5.')

class Class:
    def __init__(self,teacher,num):
        self.list = []
        self.teacher = teacher
        self.num = num

    def add_student(self,name):
        s = input('请输入需要添加的学生')
        self.lisr.append(s)

    def cha_xun(self):
        for i in self.list:
            print(i)
def main():
        while True:
            menu()
            user = input('请输入')
            if user == '1':
                add_chebgji()
            elif user == '2':
                xian_shi()
            elif user == '3':
                get_chengji()
            elif user == '4':
                set_chengji()
            elif user == '5':
                break
            else:
                print('输入有误')

class Student(Class):
    def __init__(self,name,sex,chengji_dic):
        self.name = name
        self.sex = sex
        self.chengji_dic = {}

    def add_chengji(self,):
        print('开始录入信息')
        name = input('请输入名字')
        teacher = input('请输入班主任')
        num = input('请输入班级号')
        self.chengji_dic = input('请输入成绩')

    def xian_shi(self):
        for i in self.chengji_dic:
            print('姓名是'+self.name+'班级是'+self.num+'班任是'+self.teacher+'成绩是'+self.chengji_dic)
        if len(chengji_dic) == 0:
            print('没有学生信息')

class chengji(Student):
    def __init__(self,chinese,math,english):
        self.chinese = c_v
        self.math = m_v
        self.english = e_v

    def get_chegnji(self):
        f = input('姓名')
        fi = 0
        for i in self.chengji_dic:
            if f == i[self.name]:
                print('该学生的成绩如下图%d'%self.list)
                fi = 1
                break
        if fi == 0 :
            print('找不到这个人请重新输入')

    def set_chengji(self):
        c = input('姓名')
        if c == i[self.name]:
            print(self.name+'家长您好')
        else:
            print('找不到这个人请重新输入')

    def __str__(self):
        return self.name+'同学的成绩是'+self.chengji_dic+'\t'


asd = Class('z',12)
asd.main()

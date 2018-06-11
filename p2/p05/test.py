class banji:
    def __init__(self,banming,teacher):
        self.banming=banming
        self.teacher=teacher

        self.banjilist=[]
        self.yu=[]
    def addban(self):
        self.banjilist.append(self.banming)
        self.banjilist.append(self.teacher)
    def __str__(self):
        return " 班级：%s ，班主任老师：%s" % (self.banming,self.teacher)
class student(banji):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

        self.xiangdic={}
    def studentxx(self):
        self.xiangdic["姓名"]=self.name
        self.xiangdic["年龄"]=self.age
        self.xiangdic["性别"]=self.sex

    def __str__(self):
        return "学生姓名：%s ，年龄：%s ，性别：%s " % (self.name,self.age,self.sex)

class chengji(student):
    def __init__(self,yuwen,math,english):
        self.yuwen=yuwen
        self.math=math
        self.english=english
        self.chengdic={}
    def getcha(self,cha):
        if cha=="语文":
            return self.yuwen
        elif cha=="数学":
            return self.math
        elif cha=="英语":
            return self.english
    def setgai(self,dui,zhi):
        if dui=="语文":
            self.yuwen=zhi
        elif dui=="数学":
            self.math=zhi
        elif dui=="英语":
            self.english=zhi



    def cheng1(self):
        self.chengdic["语文"]=self.yuwen
        self.chengdic["数学"]=self.math
        self.chengdic["英语"]=self.english


    def __str__(self):
        return "成绩：语文：%s 数学：%s 英语：%s " % (self.yuwen,self.math,self.english)
aa=input("你要创建的班级：")
bb=input("班主任老师：")
aa=banji(aa,bb)
aa.addban()
print(aa)
yu=aa.yu
def suoyou():
    for i in yu:
        print("学生编号：%s" % i["编号"])
        print("学生姓名：%s" % i["姓名"])
        print("学生年龄：%s" % i["年龄"])
        print("学生性别：%s" % i["性别"])
        print("学生语文成绩：%s" % i["语文"])
        print("学生数学成绩：%s" % i["数学"])
        print("学生英语成绩：%s" % i["英语"])
def chadan():
    aa=input("你要查找的学生姓名是：")
    for i in yu:
        if aa==i["姓名"]:
            print("学生编号：%s" % i["编号"])
            print("学生姓名：%s" % i["姓名"])
            print("学生年龄：%s" % i["年龄"])
            print("学生性别：%s" % i["性别"])
            print("学生语文成绩：%s" % i["语文"])
            print("学生数学成绩：%s" % i["数学"])
            print("学生英语成绩：%s" % i["英语"])
def genggai():
    aa=input("你要更改的学生姓名是：")
    bb=input("你要更改的是那项信息：")
    cc=input("你要更改为：")
    for i in yu:
        if aa==i["姓名"]:
            i[bb]=cc
            print(i)
def shanchu():
    aa=input("你要删除的学生编号是多少")
    for i in yu:
        if aa == i["编号"]:
            yu.remove(i)
            print("删除了")


a=0
while True:
    a=a+1
    cc=input("你要创建的第 %d 位学生的姓名：" % a)
    if cc=="q":
        break
    #elif cc==k
    gg=input("学生年龄：")
    ee=input("学生的性别：")
    cc=student(cc,gg,ee)
    cc.studentxx()
    print(cc)


    ff=input("该学生的语文成绩：")
    gg=input("该学生的数学成绩：")
    hh=input("该学生的英语成绩：")
    a1=chengji(ff,gg,hh)
    a1.cheng1()
    a1.chengdic.update(cc.xiangdic)
    a1.chengdic["编号"]=str(a)
    yu.append(a1.chengdic)

    while True:
        weng=input("你是否需要改动或查询此次录入成绩：1,查询2,改动  q.无任何要改动")
        if weng == "1":
            kemu=input("你要查找的科目是")
            print(a1.getcha(kemu))
            print(a1)
        elif weng == "2":
            dui=input("你要更改的科目是")
            fen=input("你要改为多少")
            a1.setgai(dui,fen)
            print(a1)
        elif weng == "q":
            break



    while True:
        ll=input("1,查询所有有人成绩2,按姓名查询一个人成绩3,更改学生信息4,删除某位学生的所有信息 q.退出")

        if ll=="1":
            suoyou()
        elif ll=="2":
            chadan()
        elif ll=="3":
            genggai()
        elif ll=="4":
            shanchu()
        elif ll=="q":
            break



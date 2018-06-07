class Worker:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def set_salary(self,new_salary):
        if new_salary > self.salary:
            self.salary = new_salary
        else :
            print('扌巨纟色')
    def get_salary(self,id):
        if id == '媳妇':
            return 1000
        elif id == '朋友':
            return 100000
        elif id == '老爹':
            return self.salary
        else :
            return 0


gtq = Worker('光头强',10000)
print(gtq.name)
while True :
    id = input('输入id')
    if id == 'q':
        print('无可奉告')
        break
    else:

#s = gtq.get_salary()
        print('光头强的工资是 %d ' % gtq.get_salary(id))

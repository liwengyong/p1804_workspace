
class House:
    def __init__(self,area,addr,):
        self.area = area
        self.addr = addr
        self.items = []

    def add_items(self,item,light):  #添加家具
        if self.area > item.area :
            self.area -=item.area
            self.items.append(item.name)
        else:
            print('床太大了，我的小家放不进去')

        if self.area >light.size:
            self.area -= light.size
            self.items.append(light.name)
        else:
            print('这个%s太大了，我这小庙容不下它'% light.name())


    def set_items(self,item):
        if item.area < self.area:
            self.area -=items.area
            self.items.append(item.name)
        else :
            print('床太大了，我的小家放不进去')

        if self.area > light.size:
            self.area -= light.size
            self.items.append(light.name)
        else:
            print('这个%s太大了，我这小庙容不下它'% light.name())

    def get_items(self,a):
        if a == 'boss':
            return '只有床'
        elif a == 'dad':
            return self.items
        elif a == 'friend':
            return '两米大床以及大吊灯'
        else:
            return 0


    def __str__(self):
        return '房子大小是%d,地址位于:%s,包含的家具有:%s'%(self.area,self.addr,str(self.items))

class Bed:
    def __init__(self,area,name):
        self.area = area
        self.name = name

    def __str__(self):
        return '%s 已经购买好了，它的大小是%s'% (self.name,self.area)


class Light:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):

        return '%s 已经购买好了，它的颜色是%s,它的大小是%d'% (self.name,self.color,self.size)


house01 = House(200,'前门北大街01')
print('新家的地址是%s '% id(house01))

baby_bed = Bed(100,'婴儿床')

#print(baby_bed)
sr_bed = Bed(200,'双人床')

#house01.add_items(sr_bed)

big_bed = Bed(300,'巨人专用')

#house01.add_items(big_bed)

dd_light = Light('360度镶钻环绕大吊灯','九彩',50)
#print(dd_light)
house01.add_items(baby_bed,dd_light)
#print(house01)
while True:
    a = input('输入来客')
    if a == 'q':
        print('无可奉告')
        break
    else:
        print('新房的家具是 %s '% house01.get_items(a))

#house01 = House(200,'前门北大街01')



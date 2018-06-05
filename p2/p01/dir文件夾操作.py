
import os

#os.mkdir('house')
#os.mkdir('../gril')

l = os.getcwd()
print(l)

os.chdir('./house')
print('修改之後的默認路徑是:%s'%os.getcwd())


f = open('1.txt','w')
os.mkdir('xiaohua')
os.rmdir('xiaohua')
os.chdir('../')
#os.rmdir('house')

import shutil
shutil.rmtree('house')

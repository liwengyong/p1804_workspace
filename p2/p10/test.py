
#import mtest.t01,mtest.t02
#mtest.t01.t()
#mtest.t02.tt()
import sys
p ='/home/nn/p1804/p2/p10'
sys.path.append(p)
print(sys.path)
from mtest.t01 import *
from mtest.t02 import *
t()
tt()

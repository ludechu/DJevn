import random
import os
def randomstr(num=6):
    list = random.sample('qwertyuio@#$%^&',Num=num)
    s = ''.join(list)
    return s
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




import os

# """调用电脑的记事本"""
# os.system('notepad.exe')
#
# """调用电脑文件"""
# os.startfile("xxx")

"""打印当前的工作路径"""
print(os.getcwd())

list1 = os.listdir("../stu")

for a in list1:

    if a.endswith('.py'):

        print(a)

print('----------------')




import os
import zipfile

# TODO 函数化，取消固定字符串
f = zipfile.ZipFile('杨帆-第六次作业-1600012427.zip', 'w', zipfile.ZIP_DEFLATED)
directory = 'Homework_6'
l = os.listdir(directory)
# TODO 用栈改造之
for file in l:
    if os.path.isdir(directory + file):
        assert False
    else:
        f.write(directory + '/' + file)
f.close()

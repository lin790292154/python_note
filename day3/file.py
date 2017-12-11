#write by Kratos
#about file action.

f = open('lyrics.txt')  # 打开文件
first_line = f.readline()
print('first line:', first_line)  # 读一行
secend_line = f.readline()
print('first line:',secend_line) # 读一行
secend_line = f.readline()
print('first line:',secend_line)
secend_line = f.readline()
print('first line:',secend_line)
secend_line = f.readline()

print('first line:',secend_line)
# print('我是分隔线'.center(50, '-'))
# data = f.read()  # 读取剩下的所有内容,文件大时不要用
# print(data)  # 打印文件

f.close()  # 关闭文件
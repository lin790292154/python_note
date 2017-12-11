#write by kratos

"""
打开文件的模式有：

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a
"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

rU
r+U
"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

rb
wb
ab
"""

f = open("yesterday.txt","a",encoding="utf-8")  #文件句柄：包含了文件的命名，字符集，它的大小，内存地址。

#data = f.read()
#data2 = f.read()

#print(data)
#print("-----------data2--",data2)

#"w":写文件模式：不可读，不存在则创建；存在则删除原来的所有内容！！！其实是新建了一个文件，覆盖了原来的文件。
#f.write("人生苦短，")
#f.write("我用python")

#"a":追加模式：不可读，不存在则创建；存在则只追加内容，不会删除原来的内容。

f.close()

f = open("yesterday.txt","r",encoding="utf-8")

##读一行
#f.readline()

##读所有内容到一个列表中，

# #把所有内容读出来返回一个列表，每行为一个元素。
# print(f.readlines())

#高效的，节省内存的，输出所有内容的方式:
count = 0
for line in f :
    print(line)

#文件的光标（指针位置）
f = open("yesterday.txt",'r',encoding="utf-8")

#光标的位置
print(f.tell())

#将光标回到你想要的位置
f.seek(0)

#打印文件的编码
print(f.encoding)

#返回内存编号
print(f.fileno())

#是否是一个tty设备，比如打印机，terminal
print(f.isatty())

#是否可以移动光标
print(f.seekable())

#文件是否可读
print(f.readable())

#文件是否可写
print(f.writable())

#强制刷新内存，将缓存中的内容强制写入到硬盘中
f.flush()

#从文件开始截断(无论当前光标的位置在哪)，不带参数就清空所有，带参数就截断到哪个位置。
#f.truncate(20)

f.close()

#文件修改
f = open("yesterday.txt","r",encoding="utf-8")  #文件句柄：包含了文件的命名，字符集，它的大小，内存地址。
f_new = open("yesterday.new.txt",'w',encoding='utf-8')

for line in f:
    if "滋味是甜的" in line:
        line = line.replace("滋味是甜的","滋味是苦的")
    f_new.write(line)

f.close()
f_new.close()
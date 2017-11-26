#write by kratos

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


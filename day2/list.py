#----------列表---------------

names = ["uzi","xiaohu","xiangguo","ming","uzi"]

#切片
print(names)
print(names[0],names[3])
print(names[1:3])	#切片（规则：顾头不顾尾）
print(names[1:-2])	#切片
print(names[2:])	#切片（从2取到最后）
print(names[:2])	#切片（从开始取到2）
print(names[0:-1:2])    #步长切片



#追加
names.append("yihang")

#插入
names.insert(1,"yihang")

#修改
names[2] = "yihang"

#删除
names.remove("xiangguo")	#按值删除
del names[1]	#按下标删除
names.pop(3)	#按下标删除

#查值的下标
names.index("xiangguo")

#清空
names.clear()

#反转
names.reverse()

#排序	(按assic码排序，字符-数字-大写字母-小写字母)
names.sort()

#扩展	（扩展后，names2依然存在，所以不叫合并）
names2 = ["xiye","meiko"]
names.extend(names2)

#复制
#  浅copy三种方法：names3 = names.copy() ,names3 = copy.copy(names) ,naemes3 = names[:] ; 只拷贝第一层，如果还有第二层列表，拷贝的第二层的列表的内存地址)
#  超浅copy： names3 = names   #这种方法拷贝列表，第一层开始都是拷贝内存地址。
names = ["uzi","xiaohu","xiangguo",["faker","bang"],"ming","uzi"]
names3 = names.copy()
names[2] = "MLXG"
names[3][0] = "guapi"

print(names)
print(names3)

#深copy,不拷贝内存地址，开辟新的内存空间复制
import copy

names3 = copy.deepcopy(names)

#列表循环
for i in names:
    print(i)



#-----------元组-------
names = ("uzi","ming")

#元组就是只读列表
#只有两个方法，一个是count一个是index
























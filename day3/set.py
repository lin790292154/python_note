#write by lincj
#about set

#初始化方式1
list_1 = [2,3,3,4,5,2,9,11]
set_1 = set(list_1) #集合也是无序的,集合天生就是去重的
print("set_1:",set_1)

#初始化方式2
set_2 = set([3,55,4,9,456,54])
print("set_2:",set_2)

#初始化方式3
set_3 = {1,3,6,7}

#交集
print("交集：",set_1.intersection(set_2))
print(set_1 & set_2)

#并集
print("并集：",set_1.union(set_2))
print(set_1 | set_2)

#差集  in set_1 not in set_2
print("差集：",set_1.difference(set_2))
print(set_1 - set_2)

#对称差集  在set_1或在set_2中，但是不会同时在二者中
print("对称差集：",set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)

len(set_1)  #set_1的长度

print(set_2 in set_1)  #测试set_2是否是set_1的成员

print(set_2 not in set_1)  #测试set_2是否不是是set_1的成员

#子集
set_1.issubset(set_2)
print(set_1 <= set_2)  #测试是否set_1中的每一个元素都在set_2中

set_1.issuperset(set_2)
print(set_1 >= set_2)  #测试是否set_2的每一个元素都在set_1中

#set_3.discard()

#增删改查
set_1.add(999)  #增加一个
set_1.update([567,346,7657])  #增加多个
set_1.update({235,436,})    #set_3.discard()
print(set_1)

set_1.pup()  #随意删一个
set_3.discard(666) #删除666，如果666存在则删除，不纯在返回None
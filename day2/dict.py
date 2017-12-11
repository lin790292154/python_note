#write by kratos
#about dict

#dict:key-value的数据类型

info = {
    'stu001':"kratos",
    'stu002':"yang",
    'stu003':"lincj"
}

print(info)
#查
#print(info["stu002"])
print(info.get("stu004"))   #安全的获取方法，直接print不存在会报错。

#增改  存在修改，不存在就增加
info["stu002"]="ming"
info["stu004"]="uzi"

#删
info.pop("stu002")
#del info["stu004"]


#多级字典嵌套及操作;key 最好用英文

info1 = {
    "RNG":{"xiaohu":[21,"gay"]},
    "EDG":{
        "clearlove":["123","4396"]
    }
}

print(info1["EDG"]["clearlove"][0])


#其他姿势

#列出所有value
print(info.values())

#列出所有keys
print(info.keys())

#参数1如果不存在就创建它，value值为参数2
info.setdefault("stu006","124356")

#更新合并:update 相同key的更新value值，没有相同的添加进info
b={"stu001":666,"stu008":32423}
info.update(b)

#初始化一个新的字典,value都为test，每个value指向的是同一个内存地址，所以在多层字典的时候，修改一个会修改所有的value
c = dict.fromkeys([4,3,9],"test")

#字典的循环
for i in info:
    print(i,info[i])





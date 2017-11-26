#write by lcj


'''
购物车
    用户入口：
    1.商品信息存在文件里，（可以尝试读出来存在列表里）
    2.已购商品，余额记录。只有第一次进入的时候需要输入工资

    商家入口：
    1.可以添加商品，修改商品价格。

可以写成两个脚本，一个用户脚本。一个商家脚本。

'''


with open('shop.txt','r',) as file1:
    salary = file1.readline()
    a = file1.read()
    shop_list = a.splitlines()
    i=0
    shop_dict={}
    while i < len(shop_list)-2:
        shop_dict[shop_list[i]]=shop_list[i+1]
        i+=2
    print(salary)

if int(salary) == 0:
    salary = int(input("welcome to shop first,please input your salary: "))

while True:
    print(shop_dict)
    choice = input("input goods name:")
    if choice in shop_dict:
        c = shop_dict[choice]
        salary = salary - int(shop_dict[choice])
        print("shopping success ,you have salary now:",salary)

    else:
        print("my shop has's it :",choice)


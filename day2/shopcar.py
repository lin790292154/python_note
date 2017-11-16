
goods = [["iphone",4600],["Macpro",4700],["Rookie",4700],["tee",998]]

salary = int(input("please input your salary:"))
goods_number_list = []
shopcar = []
while True :
    for i in goods:
        goods_number = goods.index(i)
        print(goods_number, i[0], i[1])
        goods_number_list.append(str(goods_number))
    commond_buy = input("please input goods number buy it or please input 'q' exit")
    if str(commond_buy) in goods_number_list :
        if salary >= goods[int(commond_buy)][1] :
            salary = salary - goods[int(commond_buy)][1]
            shopcar.append(goods[int(commond_buy)][0])
            print("buy goods success! you have \033[32;1m%d\033[0m salary now" % salary)
            continue
        else:
            print("Your salary not enough!")
    elif commond_buy == "q" :
        break
    else:
        print("input error!")
        continue
print(shopcar,salary)
__author__ =  "kratos"

import os
import sys
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
BASE_DIR_2 = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR_2)

from core import accout_user


def goods_list() :

        list = {"ipone":"6000",
                "candy":"998",
                "Mac Pro":"9998",
                "keyborad":"888"}
        commond = "i"
        shopping_car = []
        count = 0
        while commond != "q":
            print("good list : ",list)
            commond = input("please input your want buy good join your shopping car , input 'q' to quit ,input 'pay' to pay your bill ：")
            if commond in list :
                shopping_car.append(commond)
                count += int(list[commond])
                print(" {goods} Join success !!!! you have goods in shopping car now : ".format(goods=commond,),shopping_car)
                time.sleep(1)
                continue
            elif commond == "q" :
                print("Quit shop system ....")
                break
            elif commond == "pay" :
                n = "1"
                while n == "1" :
                    id = input("Please input your Credit car id : ")
                    n = accout_user.user_pay(id,str(count))
                exit("欢迎下次光临，再见！！！")
            else:
                print("输入错误，请重新输入")
                continue


goods_list()





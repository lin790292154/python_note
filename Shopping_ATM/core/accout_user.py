__author__ = "kratos"

import os
import sys
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def user_transfer(id):
    commond = "yes"
    while commond == "yes" :
        with open("{dir}/data/account".format(dir=BASE_DIR), "r") as f1 , \
                open("{dir}/data/account_new".format(dir=BASE_DIR), "w") as f2 :
            Credit_card = json.load(f1)
            transfer_id = input("please input you want transfer id : ")
            if transfer_id in Credit_card :
                count = input("please input you want transfer count : ")
                Credit_card[id]["balance"] = str(int(Credit_card[id]["balance"]) - int(count))
                Credit_card[transfer_id]["balance"] = str(int(Credit_card[transfer_id]["balance"]) + int(count))
                json.dump(Credit_card, f2, ensure_ascii=False, indent=4)
                os.remove("{dir}/data/account".format(dir=BASE_DIR))
                os.rename("{dir}/data/account_new".format(dir=BASE_DIR), "{dir}/data/account".format(dir=BASE_DIR))
                write_log( id , "transfer {count} to {transfer_id} ".format(count=count,transfer_id=transfer_id))
                write_log( transfer_id," received {count} from {id} ".format(count=count,id=id) )
                print("Transfer success !!!")
                break
            else:
                commond = input("Accout not exsit ,input 'yes' continue ,input 'no' quit ")

def write_log(id,message) :
    with open("{dir}/log/{id}.log".format(dir=BASE_DIR, id=id), "r") as f1 , \
            open("{dir}/log/{id}.log_new".format(dir=BASE_DIR, id=id), "w") as f2 :
        now = time.strftime("%Y-%m-%d %X", time.localtime())
        mes_log = json.load(f1)
        mes_log[now] = message #" received {count} from {id} ".format(count=count,id=id)
        json.dump(mes_log,f2, ensure_ascii=False, indent=4)
        os.remove("{dir}/log/{id}.log".format(dir=BASE_DIR, id=id))
        os.rename("{dir}/log/{id}.log_new".format(dir=BASE_DIR, id=id),"{dir}/log/{id}.log".format(dir=BASE_DIR, id=id))

user_transfer("004")




__author__ = "kratos"

"""
要求:
1.search
2.add
3.del
4.
eval()   ##能将字符串转成字典

新建的时候需要判断，是否存在该记录，存在跳过，不存在添加

"""
def search_conf(x) :
    with open( "HA_conf" , 'r',encoding = 'utf-8') as f1 :
        count = 0
        n = 0
        for line in f1 :
            count += 1
            if n != 0 :
                print(line)
                n = 0
            if x  in line :
                n = count + 1

def add_conf(x) :
    with open( "HA_conf" , 'a',encoding = 'utf-8') as f1 :
        x = eval(x)
        f1.write("\nbackend {backend}\n        server {server} weight {weight} maxconn {maxconn}".format(
            backend = x.get("backend"),
            server = x.get("record").get("server"),
            weight = x.get("record").get("weight"),
            maxconn = x.get("record").get("maxconn")))

def del_conf(x) :
    with open( "HA_conf" , 'r',encoding = 'utf-8') as f1 ,open( "HA_conf_new" , 'w',encoding = 'utf-8') as f2:
        x = eval(x)       
        count = 0
        m = 0
        list_1 = []
        for line in f1 :
            count += 1
            if m == 1 :
                if  str(x.get("record").get("server")) in line and str(x.get("record").get("weight")) in line and str(x.get("record").get("maxconn")) in line :
                    continue
                else:
                    f2.write(p)
                    f2.write(line)
                    m = 0
            else:
                if x.get("backend") in line and "backend" in line :
                    m = 1
                    p = line
                else:
                    f2.write(line)







# search_conf("backend www.oldboy.org")
# add_conf('''{
#             'backend': 'www.mage.org',
#             'record':{
#                 'server': '100.1.11.9',
#                 'weight': 88,
#                 'maxconn': 34
#             }
#         }''')

del_conf('''{
            'backend': 'www.mage.org',
            'record':{
                'server': '100.1.11.9',
                'weight': 88,
                'maxconn': 34
            }
        }''')
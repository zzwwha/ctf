#!/usr/bin/python3

def zhalan(txt,key):
    s = ''
    for m in range(key):
        for n in range(m,len(txt),key):
            s = s + txt[n]
    return s

if __name__ =='__main__':
    txt = input('请输入明文或密文：').strip()
    key = []
    for i in range(2,len(txt)):
        if len(txt)%i==0:
            key.append(i)
    for j in key:
        flag = zhalan(txt,j)
        print(f'{j}栏：{flag}')

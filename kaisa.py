#!/usr/bin/python3

txt = input('请输入密文：').strip()
n = input('您是否需要推荐明文(Y/N)：').strip()

for i in range(1,26):
        plain = ''
        for j in txt:
                if j.islower():
                        plain = plain + chr(97+(ord(j)-i-97)%26)
                elif j.isupper():
                        plain = plain + chr(65+(ord(j)-i-65)%26)
                else:
                        plain = plain + j
        if n.lower() == 'y':
            
                key = ('flag','ctf','key','the','is','no','for','than','have','to')
                for m in key:
                        if m in plain:
                                print('明文可能是：',plain)
                                print()
                                break
        elif n.lower() == 'n':
                print(plain)
                print()

# 考拉商品图片转移测试
import re
with open("kaola_url.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
    n = 0
    for line in lines:
        line = line.lower()
        #通过正则表达式,判断图片名称相同，则通过测试
        new = re.findall(r"kaola/(.*?).jpg", line)
        if new == []:
            new = re.findall(r"kaola/(.*?).png", line)

        # old = re.findall(r"netease.com/(.*?).jpg|netease.com/(.*?).png|127.net/(.*?).png|127.net/(.*?).jpg", line)
        old =  re.findall(r"netease.com/(.*?).jpg",line)
        if old == []:
            old = re.findall(r"netease.com/(.*?).png", line)
        if old == []:
            old = re.findall(r"127.net/(.*?).png", line)
        if old == []:
            old = re.findall(r"127.net/(.*?).jpg", line)

        if new[0] != old[0]:
            print("图片对应不上")

print("测试完成")







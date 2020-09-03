import tkinter as tk
import time,random
from datetime import datetime
user =  ['a','b','c','d','e']

class LoveYou():

    def __init__(self):
        #建立窗口
        self.window = tk.Tk()
        self.window.title('LoveYou')
        self.window.geometry('800x800')
        self.text =  tk.StringVar()
        self.count = tk.StringVar()

        d=datetime.today()     #获取当前日期时间
        self.day = d.isoweekday()

    def take(self):
        '''
        负责随机抽取同学提问
        :return:
        '''

        for s in range(50):
            '''
            后几秒慢点，制造紧张气氛
            '''
            desc = ''
            if s == 47:
                time.sleep(0.6)
            elif s == 48:
                time.sleep(0.7)
            elif s == 48:
                time.sleep(0.8)
            elif s == 49:
                time.sleep(0.9)
            else:
                time.sleep(0.05)

            classes = random.sample(user, 2)
            desc += "呦,你被上帝选中了:%s\n" % classes[0]
            desc += "呦,你看着也很不错呀:%s\n" % classes[1]


            self.text.set(desc)  # 设置内容
            self.window.update()  # 屏幕更新

    def kill(self):
        '''
        负责根据星期几选择不同惩罚遍数
        :return:
        '''

        if self.day == 1:
            count = random.randint(50, 100)
            kill_desc = "上帝奖励了你们组%d遍" % (count)

        elif self.day == 2:
            count = random.randint(50, 120)
            kill_desc = "上帝奖励了你们组%d遍" % (count)
            self.count.set(kill_desc)
        elif self.day == 3:
            count = random.randint(50, 140)
            kill_desc = "上帝奖励了你们组%d遍" % (count)
        elif self.day == 4:
            count = random.randint(50, 160)
            kill_desc = "上帝奖励了你们组%d遍" % (count)
            self.count.set(kill_desc)
        elif self.day == 5:
            count = random.randint(50, 180)
            kill_desc = "上帝奖励了你们组%d遍" % (count)
        else:
            kill_desc = '周末就别提问了'

        self.count.set(kill_desc)  # 设置内容
        self.window.update()  # 屏幕更新

    def main(self):
        '''
        主函数负责绘制
        :return:
        '''

        # 绘制筛选信息
        l2 = tk.Label(self.window, fg='red', textvariable=self.text, width=500, height=3)
        l2.config(font='Helvetica -%d bold' % 30)
        l2.pack()

        # 绘制惩罚信息
        l3 = tk.Label(self.window, fg='red', textvariable=self.count, width=500, height=3)
        l3.config(font='Helvetica -%d bold' % 20)
        l3.pack()

        # 绘制筛选按钮
        btntake = tk.Button(self.window, text="筛选", width=15, height=2, command=self.take)
        btntake.pack()

        # 绘制惩罚按钮
        btnkill = tk.Button(self.window, text="惩罚", width=15, height=2, command=self.kill)
        btnkill.pack()

        # 进入循环
        self.window.mainloop()


if __name__ == '__main__':
    loveyou = LoveYou()
    loveyou.main()

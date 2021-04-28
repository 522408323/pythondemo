'''
计时器
start和stop方法代表启动和停止


'''
import time as tt
class MyTimer():

    def __init__(self):
        self.unit =['年','月','日','小时','分钟','秒']
        self.prompt = "未开始"
        self.begin = 0
        self.end = 0
        self.lasted = []

    def start(self):
        self.begin = tt.localtime()
        print("计时开始")

    def stop(self):
        self.end = tt.localtime()
        self._calc()
        print("计时结束")

    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for i in range(6):
            self.lasted.append(self.end[i] - self.begin[i])
            #print(self.lasted[i])
            if self.lasted[i]:
                self.prompt += str(self.lasted[i]) + self.unit[i]
        print(self.prompt)

    def __str__(self):
        return self.prompt

    def ccc(self):
        for i in range(100000000):
            pass
t1 = MyTimer()
print(t1) # 未开始
t1.start()# 计时开始
t1.ccc()
t1.stop()#计时结束


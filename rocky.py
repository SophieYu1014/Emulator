from time import sleep as slp
import numpy as np
import datetime


def repeat(i):
    string = "今天是第%d天" % i
    print(string)
    eat()
    sleep()
    code()
    i += 1

    # Calling a function inside itself, this is called RECURSION.
    if i < 3:
        repeat(i)

    print(i)


def get_date():
    today = datetime.datetime.now()
    print(today.date())

def eat():
    menu = ['咖喱鸡肉','香锅','火锅','Sophie']
    index = np.random.randint(0,4)
    weight = np.random.randint(500,2000)
    # Regex expression, %d - Integer, %s - String
    string = "今天Rocky吃了%s, 一共%d卡路里" % (menu[index], weight)
    print(string)

def sleep():
    time = np.random.randint(300,600)
    hr, m = divmod(time, 60)
    string = "今晚Rocky睡了%d小时%02d分钟" % (hr, m)
    print(string)

def code():
    loc = np.random.randint(0,400)
    string = '今天Rocky写了%d行代码\n' % loc
    print(string)


repeat(0)

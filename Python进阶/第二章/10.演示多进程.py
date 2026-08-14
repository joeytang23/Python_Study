"""
多进程目的:
    它属于多任务的一种实现方式,未来充分利用CPU资源\\

实现方式:
    1.导入包
    2.创建进程对象,关联目标函数
    3.启动进程
"""

import multiprocessing
import time
def coding():
    for i in range(10):
        time.sleep(0.1)
        print(f"正在做第{i}次代码练习")

def music():
    for i in range(10):
        time.sleep(0.1)
        print(f"正在听第{i}边音乐....")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)
    p1.start()
    p2.start()
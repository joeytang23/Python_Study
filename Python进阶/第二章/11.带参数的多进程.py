"""
案例:演示带参数的多进程

进程传参的两种方式:
    1.args,接受位置参数
    2.kwargs,关键字参数/
"""
import multiprocessing
import time
def coding(name,num):
    for i in range(num):
        time.sleep(0.1)
        print(f"{name}正在做第{i}次代码练习")

def music(name,count):
    for i in range(count):
        time.sleep(0.1)
        print(f"{name}正在听第{i}次音乐鉴赏.........")

if __name__ == '__main__':
    p1=multiprocessing.Process(target=coding,args=('虚竹',10))
    p2=multiprocessing.Process(target=music,kwargs={'count':10,'name':"博崽"})
    p1.start()
    p2.start()

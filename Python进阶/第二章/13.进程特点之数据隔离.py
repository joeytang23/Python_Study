"""
案例: 演示进程的特点.

进程的特点:
    1. 进程之间数据是相互隔离的.
        因为子进程相当于是父进程的"副本", 会将父进程的"main外资源"拷贝一份, 即: 各是各的.
    2. 默认情况下, 主进程会等待子进程执行结束再结束.
"""
import multiprocessing
import time

my_list=[]

def write_data():
    for i in range(1,6):
        my_list.append(i)
        print(f"添加数据{i}")

    print(f"write_data函数:{my_list}")

def read_data():
    time.sleep(3)
    print(f"read_data函数:{my_list}")

#每创建一个进程就走一遍代码，三次打印
print('main外资源')

if __name__ == '__main__':
    p1=multiprocessing.Process(target=write_data)
    p2=multiprocessing.Process(target=read_data)
    p1.start()
    p2.start()

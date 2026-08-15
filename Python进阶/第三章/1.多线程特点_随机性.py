"""
案例: 演示多线程特点.

多线程特点:
    1. 线程执行具有随机性, 原因是CPU在做着高效的切换.
    2. 默认情况下, 主线程会等待子线程结束再结束.
    3. (同一个进程的)线程间 数据共享。
    4. 多线程操作共享数据， 可能会出现安全问题， 可以用 互斥锁解决。

CPU调度资源的策略：
    1.均分时间片
    2.抢占式调度
"""
# 需求: 创建多个线程, 多次运行, 观察结果.
import threading
import time

def print_info():
    time.sleep(0.2)
    #获取当前线程对象
    current_thread = threading.current_thread()
    print(current_thread.name)

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=print_info)
        t.start()
"""
案例: 演示多线程特点之 守护线程.

多线程特点:
    1. 线程执行具有随机性, 原因是CPU在做着高效的切换.
    2. 默认情况下, 主线程会等待子线程结束再结束.
    3. (同一个进程的)线程间 数据共享。
    4. 多线程操作共享数据， 可能会出现安全问题， 可以用 互斥锁解决。

"""
import threading,time
def work():
    for i in range(10):
        time.sleep(0.2)
        print("working...")

if __name__ == '__main__':
    t = threading.Thread(target=work,daemon=True)
    #2 t = threading.Thread(target=work)
    # t.daemon = True

    t.start()
    time.sleep(1)
    print("main线程已经结束")

"""
单任务演示,前边不执行完后边不会执行
"""

def func_a():
    for i in range(10):
        print("hello world")

def func_b():
    for i in range(2):
        print("hello python")

func_a()
print("-"*23)
func_b()
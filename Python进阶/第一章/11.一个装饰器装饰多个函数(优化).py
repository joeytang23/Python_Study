"""
案例:展示 带参数的装饰器

要点:
    1.一个装饰器只能有一个参数
    2.如果装饰器多个参数,可以在外面再包裹一层
"""


# 需求:定义一个可以装饰加法和减法的装饰器

def my_decorator(fn_name):
    def fn_inner(a,b):
        if fn_name.__name__ == 'get_sum':
            print("正在努力计算[加法]中")
        elif fn_name.__name__ == 'get_sub':
            print("正在努力计算[减法]中")
        return fn_name(a,b)
    return fn_inner


@my_decorator
def get_sum(a,b):
    return a+b

@my_decorator
def get_sub(a,b):
    return a-b

print(get_sum(1,2))
print(get_sub(1,2))
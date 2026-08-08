"""
    装饰器的内部函数格式要和被装饰的原函数保持一致
    即原函数无参无返回,则内部函数必须也是
    同理
"""

#需求:无参无返回值的getsum求和函数,不改变功能的基础上,添加友好提示
#定义装饰器
def my_decorator(fn_name):
    def fn_inner(x,y):
        print(f"正在努力计算{x}+{y}的值")
        fn_name(x,y)
    return fn_inner

#定义原函数
@my_decorator
def getsum(a,b):
    sum=a+b
    print(f"{a}+{b}={sum}")


getsum(10,20)

getsum = my_decorator(getsum)
getsum(10,20)



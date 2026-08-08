"""
    装饰器的内部函数格式要和被装饰的原函数保持一致
    即原函数无参无返回,则内部函数必须也是
    同理
"""

#需求:无参无返回值的getsum求和函数,不改变功能的基础上,添加友好提示
#定义装饰器
def friendly_support(fn_name):
    def fn_inner():
        print("正在努力计算")
        fn_name()
    return fn_inner

@friendly_support
def getsum():
    a=10
    b=20
    sum=a+b
    print(f"{a}+{b}={sum}")

getsum()

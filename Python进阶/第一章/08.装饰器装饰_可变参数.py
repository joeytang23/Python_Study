"""
    装饰器的内部函数格式要和被装饰的原函数保持一致
    即原函数无参无返回,则内部函数必须也是
    同理
"""

#需求:定义一个可以计算多个数据和字典value值和的函数,不改变功能的基础上,添加友好提示
#定义装饰器
def my_decorator(fn_name):
    def fn_inner(*args, **kwargs):
        print("正在努力计算中")
        return fn_name(*args, **kwargs)
    return fn_inner

#定义原函数
@my_decorator
def getsum(*args,**kwargs):
    '''
    该函数用于计算数字列表和字典value值之和,

    Args:
        *args: 数字列表,接受所有位置参数,封装到元组
        **kwargs: 字典,接受关键字参数,封装到字典

    Returns:结果之和

    '''
    return sum(args) + sum(kwargs.values())


#测试
sum = getsum(1,2,3,a=4,b=5)
print(sum)
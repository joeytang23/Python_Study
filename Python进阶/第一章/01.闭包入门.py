"""
    概述:
        内部函数 使用了外部函数的变量
    格式:
        def 外部函数(形参列表):
            外部函数的变量

            def 内部函数():
                使用外部函数的变量

            return 内部函数名
    前提条件:
        有嵌套, 外部函数嵌套内部函数
        有引用, 内部函数使用外部函数变量
        有返回  外部函数返回内部函数名
注意:
    1.函数名和函数名()这两个概念,前者是对象,后者是调用函数获取返回值
"""

def get_sum(a, b):
    return a + b

print(get_sum(1, 2))
print(get_sum)

#函数名可以赋值给变量,
my_sum = get_sum
print(my_sum)
print(my_sum(100,200))
print("-" *23)

#定义求和的闭包
def fun_outer(num1):
    def fun_inner(num2):
        sum =  num1 + num2
        print(f"求和结果{sum}")
    return fun_inner

fun_inner = fun_outer(10)
fun_inner(20)
fun_inner(20)
fun_inner(20)

fun_outer(30)(50)

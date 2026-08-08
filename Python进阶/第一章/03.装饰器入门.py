"""
案例:装饰器入门

装饰器介绍:
    概述和作用:
        本质是个闭包函数,目的是不改变原有函数的基础,对函数增强

    前提条件:
        有嵌套 有引用 有返回 有额外功能
    用法:
        格式1:传统写法
            装饰后的函数名 = 装饰器名(被装饰的函数名)
            装饰后的函数名()
        格式2:语法糖
            在要被装饰的函数上直接写@加装饰器名字
"""

#需求:发表评论前需要登陆

#1.定义外部函数,形参列表接受要被装饰的
def check_login(fn_name):
    #定义内部函数
    def fn_inner():
        print("校验登录....登陆成功.")
        fn_name()
    return fn_inner

#2.定义函数,表示发表评论
@check_login
def comment():
    print("发表评论")

@check_login
def payment():
    print("充值")

# 传统方法
# comment= check_login(comment)
# comment()

comment()
payment()
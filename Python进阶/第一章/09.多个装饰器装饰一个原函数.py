"""
案例:演示多个装饰器装饰1个函数:

记忆:
    按照由内到外的顺序来装饰
"""

#需求:发表评论前先登录再验证验证码
def check_login(fn_name):
    def fn_inner():
        print("登录校验成功")
        fn_name()
    return fn_inner

def check_code(fn_name):
    def fn_inner():
        print("验证码验证中")
        fn_name()
    return fn_inner

@check_login
@check_code
def comment():
    print("发表评论")
#
# comment = check_code(comment)
# comment = check_login(comment)
comment()
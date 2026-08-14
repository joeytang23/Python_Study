"""
案例:编码与解码

细节:
    1.编码: '字符串'.encode(码表)
    2.解码: 二进制.decode(码表)
    3.英文字母,数字,特殊符号在任意码表都是一个字节,中文在gbk两个字节,在u8三个字节
    4.
"""

s1 = '博崽abc123!@#'
print(s1)
print(s1.encode('gbk'))
print(s1.encode('utf-8'))
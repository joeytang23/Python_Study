"""
案例:文件上传客户端

服务器端开发流程:
    1.创建客户端socket对象
    2.连接服务器端IP端口号
    3.关联数据源文件,读取内容写给服务器端
    4.释放资源
注意:
    客户端和服务器端的交互是通过字节流bytes的形式实现的
"""
import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',6666))
with open('E:/Desktop/新建文件夹/提示词.txt','rb') as src_f:
    while True:
        data = src_f.read(8192)
        client_socket.send(data)
        if len(data)==0:
            break

client_socket.close()
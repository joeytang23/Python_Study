"""
案例:服务器端给客户端发送消息,客户端回复

服务器端开发流程:
    1.创建服务器端socket对象
    2.绑定IP地址和端口号
    3.设置最大监听数
    4.等待客户端建立连接
    5.给客户端发送信息
    6.接收客户端信息并打印
    7.释放资源

注意:
    客户端和服务器端的交互是通过字节流bytes的形式实现的
"""
import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',8080))
server_socket.listen(5)
accept_socket,client_info = server_socket.accept()
accept_socket.send(b"Welcome to the server!")
data = accept_socket.recv(1024).decode('utf-8')
print(f"服务器端收到{data},来自{client_info}")
accept_socket.close()

#设置端口号复用,目的是:快速重启服务器(服务器关闭后立即释放端口)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
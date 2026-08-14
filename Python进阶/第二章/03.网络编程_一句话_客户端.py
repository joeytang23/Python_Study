"""
案例:

服务器端开发流程:
    1.创建客户端socket对象
    2.连接服务器端,指定服务器端IP和端口号
    3.接受服务器端的信息并打印
    4.给服务器端发送消息
    5.释放资源


注意:
    客户端和服务器端的交互是通过字节流bytes的形式实现的
"""
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))
data=client_socket.recv(1024).decode('utf-8')
print(f"客户端收到信息:{data}")
client_socket.send('不要回答!'.encode('utf-8'))
client_socket.close()

"""
案例:演示socket对象的创建

"""
import socket
#参数1: Address Family,地址族 默认值:AF_INEF(IPv6)
#参数2:socket类型,即TCP OR UDP
socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(socket_obj)
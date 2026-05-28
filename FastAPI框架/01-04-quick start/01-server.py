# web应用开发：遵循HTTP协议
import socket

# 创建socket对象，语法：socket.socket(family,type)，family参数为AF_INET，type参数为SOCK_STREAM，()为默认值
sock = socket.socket()

# 绑定ip和端口：语法：socket.bind(address)，address参数为元组，(ip,port)
sock.bind(("127.0.0.1",8080))
sock.listen(5)                  #  监听，默认最大5个，满时阻塞，阻塞结束
while 1:
    # 接收客户端连接，语法：socket.accept()
    conn,addr = sock.accept()    # 阻塞等待客户端接收

    # 接收数据，语法：socket.recv(size)，size参数为接收数据的最大字节数，默认为1024字节
    data = conn.recv(1024)
    print("客户端发送的请求信息：\n",data)

    # 发送数据，语法：socket.send(data)，data参数为发送的数据，可以是字符串，也可以是字节串
    # b： bytes。默认发送字符串，需要转换成字节串。
    # 要遵循http协议的响应格式发送。像这样conn.send(b"hello world")写则会响应无效
    conn.send(b'HTTP/1.1 200 ok\r\nserver-name:yuan\r\ncontent-type:application/json\r\n\r\n{"user":12,"pwd":456}')

    # 关闭连接，语法：socket.close()
    conn.close()
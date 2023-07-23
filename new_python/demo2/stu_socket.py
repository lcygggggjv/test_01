from socket import *

# 定义空主机号，服务端不需要
host = ''

buff_size = 1024

port = 9876

# 将host和port封装一个元组里
addr = (host, port)

# 创建socket对象， AF_INET,表示 ip v4 ， AF_INET6  表示 ip v6, SOCK_STREAM 表示tcp

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 使用bind方法绑定端口号
tcp_server_socket.bind(addr)

# 监听端口号
tcp_server_socket.listen()
print('server port;9876')
print("正在等待客户端连接")

# 这里等待客户端连接，可能会程序被阻塞吗，直到接收到客户端连接请求，才好往下执行

# 接收客户端请求，同时返回客户端socket 和客户端端口号
tcp_client_socket, addr = tcp_server_socket.accept()
print('客户端已经连接', 'addr', '= ', addr)
# 开始读取客户端发送过来的数据，每次最多不会超过buff_size1024字节数据
# 如果超过1024，那么recv 方法只会返回buff_size个字节，剩下的会等待recv方法的下一次读取

data = tcp_client_socket.recv(buff_size)
# recv方法返回了字节形式的数据，如果使用字符串，需要将其解码，使用utf-8
print(data.decode('utf8'))

# 向客户端以utf-8发送数据

tcp_client_socket.send('你好， 我是lcy'.encode(encoding='utf-8'))

# 关闭客户端socket
tcp_client_socket.close()

# 关闭服务端socket
tcp_server_socket.close()

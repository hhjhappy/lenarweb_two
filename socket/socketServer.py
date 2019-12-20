import socket
from threading import Thread

ADDRESS = ('0.0.0.0',666)
g_socket_server  = None
g_conn_pool = []#用来存放客户端的socket

def init():
    '''
    初始化服务端
    '''
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5)
    print('服务端已经启动，等待连接...')

def accept_client():
    '''
    接受新连接
    '''
    while True:
        client,_ = g_socket_server.accept()#阻塞，等待客户端连接
        #加入连接池
        g_conn_pool.append(client)
        #给每个客户创建一个独立的线程进行管理
        thread = Thread(target=message_handle,args=(client,))
        #设置成守护进程
        thread.setDaemon(True)
        thread.start()

def message_handle(client):
    '''
    消息处理 
    '''
    client.sendall('服务器连接成功！'.encode('utf8'))
    while True:
        try:
            bytes = client.recv(1024)
            print('客户端消息',bytes.decode(encoding='utf8'))
        except ConnectionResetError as err:
            pass
        if len(bytes) == 0:
            client.close()
            g_conn_pool.remove(client)
            print('客户端下线了')
            break

if __name__ == '__main__':
    init()
    #新开一个县城，用于接收新的连接
    thread = Thread(target=accept_client())
    thread.setDaemon(True)
    thread.start()
    #主线程逻辑
    while True:
        cmd = input('''
        1、查看当前在线人数
        2、关闭服务器
        ''')
        if cmd == 1:
            print('当前在线人数：',len(g_conn_pool))
        if cmd == 2:
            exit()























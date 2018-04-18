#!/usr/bin/env

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpClisock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpClisock.recv(BUFSIZ)
        if not data:
            break
        tcpClisock.send(
            bytes('[%s] %s' % (ctime(), data), 'utf-8'))

    tcpClisock.close()
tcpSerSock.close()

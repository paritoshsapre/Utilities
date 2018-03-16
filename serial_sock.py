import socket
import serial
import thread
import time

host = 'localhost'
port = 8001

COMport = 'COM9'
COMbaud = 115200

buffSize= 4096
serial_connect_timeouts = 1
socket_connect_timeouts = 1


### create socket instance ###
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)

ser_err = 0
sock_err = 0

### create serial instance ###
print "connect serial First , Waiting ..."

while True:

    try:
        ser = serial.Serial(
        COMport,
        COMbaud,
        timeout=None,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        writeTimeout = 0,
        dsrdtr =False,
        rtscts =False,
        xonxoff =False)
        break
    except:
        print ser.isOpen()
        print "Attempting to connect:",serial_connect_timeouts 
        time.sleep(1)
        serial_connect_timeouts+=1
print "Connected."
print "Connecting Socket..."
while True:

    try:
        conn, remoteAddr = serverSocket.accept()
        break
    except:
        print "No request: waiting ...",socket_connect_timeouts
        socket_connect_timeouts+=1


def ser2sock(serial_h,socket_h):
    while True:
        data_ser = serial_h.read(32)
        socket_h.send(data_ser)
        

def sock2ser(serial_h,socket_h):
    while True:
        data_sock = socket_h.recv(32)
        serial_h.write(data_sock)
print 'Connected'
s2s1 = thread.start_new_thread(ser2sock,(ser,conn))
print 'serial to socket stream: UP'
s2s2 = thread.start_new_thread(sock2ser,(ser,conn))
print 'socket to serial stream: UP'


while True:
    pass


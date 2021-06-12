import pickle
import socket
import struct
import cv2

ip = '192.168.43.34'
port = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))
s.listen(5)

conn, addr = s.accept()
data = b''  
payload_size = struct.calcsize("=I")  
print("Connected from " + str(addr))



while True:    
    while len(data) < payload_size:
        data += conn.recv(4096) 
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("=I", packed_msg_size)[0]  
    # print(msg_size)
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    frame = cv2.resize(frame, (480, 288))
    cv2.imshow('Reciving Video', frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()
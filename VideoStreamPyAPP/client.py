import cv2
import numpy as np
import socket
import sys
import pickle
import struct

# cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.43.34',8089))

while True:
    cap=cv2.VideoCapture(0)
    ret,frame=cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("I", len(data))
    clientsocket.sendall(message_size + data)
    cv2.imshow('Transfering video', frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()
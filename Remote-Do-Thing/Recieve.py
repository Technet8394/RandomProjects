import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.IN)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

# 2 = PLED+
# 3 = PLED-
# 14 = PSWITCH+
# 15 = PSWITCH-

HOST = "192.168.1.1" 
PORT = 34120 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
       if GPIO.input(2): =True
       else :exit
       GPIO.output(14, True)
    exit

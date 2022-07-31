import socket
import random

random.seed()

# establishing server
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
random_reading_from_device = random.randint(10000, 20000)
MESSAGE = random_reading_from_device

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

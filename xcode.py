

import requests,os
from colorama import Fore,init

init(autoreset=True)

g = Fore.GREEN
r = Fore.RED
b = Fore.RED
w = Fore.GREEN

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
banner = """
{}

	   _  __      ______          __
	  | |/ /     / ____/___  ____/ /__     [{}+{}] Arthur  : Acep Xploit
	  |   /_____/ /   / __ \/ __  / _ \    [{}+{}] Web     : https://acepcyber.my.id
	 /   /_____/ /___/ /_/ / /_/ /  __/    [{}+{}] Tools   : Free For You :b
	/_/|_|     \____/\____/\__,_/\___/
                                   
 {}=============================={}
 [{}1{}] Bing Dork Scanner
 [{}2{}] Bing Dork Maker
 [{}3{}] Domain To IP
 [{}4{}] Reverse Ip Unlimited
 
"""

print(banner.format(g,b,g,w,r,b,g,r,g,r,g,r,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g))

tool = raw_input(g + "["+r+"*"+g+"] Choose tool : ")

if tool == "1":
	os.chdir("dork")
	
	os.system("python scan.py ")
	
elif tool == "2":
	os.chdir("dork")
	os.system("python maker.py")
	
elif tool == "3":
	os.chdir("dork")
	os.system("python ip.py")
		
elif tool == "4":
	os.chdir("dork")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python rev.py " + sitelist)
	

else:
	pass

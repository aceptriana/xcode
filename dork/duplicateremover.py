import os
from colorama import Fore,init

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE


print("""{}
	   _  __      ______          __
	  | |/ /     / ____/___  ____/ /__     [{}+{}] Arthur  : Acep Xploit
	  |   /_____/ /   / __ \/ __  / _ \    [{}+{}] Web     : https://acepcyber.my.id
	 /   /_____/ /___/ /_/ / /_/ /  __/    [{}+{}] Tools   : Duplicate Remover
	/_/|_|     \____/\____/\__,_/\___/
                                 

""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

lines_seen = set()
outfile = open('sites.txt', "a")
infile = open('sitelist.txt', "r")
for line in infile:
	if line not in lines_seen:
		outfile.write(line)
		lines_seen.add(line)
outfile.close()
infile.close()
if os.name == "nt":
	os.system("del sitelist.txt")
else:
	os.system("rm -rf sitelist.txt")
print("[{}+{}] Duplicate sites removed successfully!".format(settings.r,settings.y))
print("\n[{}+{}] Sites saved as {}sites.txt{}!".format(settings.r,settings.y,settings.b,settings.y))
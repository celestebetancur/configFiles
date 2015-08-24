#!/usr/bin/python

import getpass as P
from subprocess import Popen, PIPE

password = P.getpass("Password:\n")

print("Password Maker 0.1\n\nWhat password do you want?")

p = str(raw_input("(write ASCII character please)\n"))+str(password) 
e = int(raw_input("choose an encrypt level -int value-\n"))

alpha = "a!b#c$d&e=f?ghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ"

if e >= len(alpha):
	e = e % len(alpha) 

def cryp(password,level):
	level = int(level)
	toReturn = ""
	for char in password:
		index = alpha.find(char) + level
		toReturn = toReturn +  alpha[index]   	
	return toReturn

copy = Popen(['pbcopy','w'], stdin=PIPE, close_fds=True)
copy.communicate(input=cryp(p,e))	

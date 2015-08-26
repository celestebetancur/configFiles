#!/usr/bin/python

import getpass as P
from subprocess import Popen, PIPE

password = P.getpass("Password:\n")
second = P.getpass("Confirm password:\n")

if password == second:

    print("Password Maker 0.1\n\nWhat password do you want?")

    p = str(input("(write ASCII character please)\n"))+str(password) 
    e = int(input("choose an encrypt level -int value-\n"))

    alpha = "a!b#c$d&e=f?ghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ"

    if e >= len(alpha):
        e = e % len(alpha) 
else:
    print("Wrong password")

def cryp(password,level):
    level = int(level)
    toReturn = ""
    for char in password:
        index = alpha.find(char) + level
        toReturn = toReturn +  alpha[index]       
    return toReturn


pp = Popen(['xclip','-selection','c'],stdin=PIPE,close_fds=True)
pp.communicate(input=cryp(p,e).encode('utf-8'))

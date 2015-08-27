#!/usr/bin/python

from subprocess import call

print("\nHi essteb\n\n")

def enviroment(init):
    if init == "help":
        print("""\nMIR - ipython notebook\n\
navigate - (1) open chromium (2) open palemoon\n""")
    if init == "MIR":
        call(["ipython","notebook"])
    elif init == "navigate":
        i = int(input("chrome(1) or palemoon(2):\n"))
        if i == 1:
            call(["chromium",str(input("URL: "))])
        elif i  == 2:
            call(["palemoon",str(input("URL: "))])
        else: 
            print("press 1 or 2")
            callEnv()
    elif init == "navigate --mail":
        call(["chromium","www.hotmail.com","www.gmail.com"])
    elif init == "exit":
        pass
    else:
        print("Wrong input")
        callEnv()
    
def callEnv():
    initEnv = str(input("How do you want your enviroment today?\n"))
    enviroment(initEnv)
    
callEnv()

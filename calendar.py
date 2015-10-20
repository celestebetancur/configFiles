#!/usr/bin/python

import csv

def init():
    options = raw_input("read or write calendar? (r , w, all, exit) ")
    return options

def printAll():
    with open("calendar.csv","r") as c:
        fields = ["date","hour","activity","priority"]
        reader = csv.DictReader(c,fieldnames=fields,delimiter=";")

        for row in reader:    
            print row
    
def read():
    field = raw_input("Field: ")
    query = raw_input("Parameter: ")

    with open("calendar.csv","r") as c:
        fields = ["date","hour","activity","priority"]
        reader = csv.DictReader(c,fieldnames=fields,delimiter=";")

        for row in reader:
        
            if  row[field] == query:
                print row

def write():
    data = [raw_input("Date: ").lower(),raw_input("Hour: ").lower(),raw_input("Activity: ").lower(),raw_input("Priority: ").lower()]

    with open("calendar.csv","a") as c:
        writer = csv.writer(c,delimiter=";")

        writer.writerow(data)
      
options = init()

if options == "r":
    read()
elif options == "w":
    write()
elif options == "all":
    printAll()
elif options == "exit":
    pass
else:
    print "wrong input"
    init()

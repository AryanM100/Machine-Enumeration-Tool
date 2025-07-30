#!/bin/python3

import sys

filename = "/home/ryan/HackinStuff/IS/MET/nmap"
loc = "/home/ryan/HackinStuff/IS/MET/ver"
a = ""
b = ""
ports = []

with open(filename) as f:
  for line in f:
    if(line[0].isdigit() and "/" in line):
      a += line
      ports.append(line.split('/')[0])
      
with open(loc, "w") as file:
  file.write(a)

#print(a)
print(ports)
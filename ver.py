#!/bin/python3

import sys

filename = "Text/nmap"
loc = "Text/ver"
a = ""
b = ""
ports = []
service = []
ps = {}

with open(filename) as f:
  for line in f:
    if(line[0].isdigit() and "/" in line):
      line = " ".join(line.split()) + "\n"
      a += line
      ports.append(line.split('/')[0])
      service.append(line.split()[2])

with open(loc, 'w') as file:
  file.write(a)

ps = dict(zip(ports, service))

#print(a)
print(ps)
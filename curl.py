#!/bin/python3

import sys
import subprocess
import ast

ip = sys.argv[1]
ps = sys.argv[2]
ps = ast.literal_eval(ps)
ports = list(ps.keys())
service = list(ps.values())
a = ""
b = ""
c = 0

with open('Text/curl.txt', 'w') as file:
  file.write("")

with open('Text/ffuf') as file:
  for line in file:
    line = " ".join(line.split()) + "\n"
    if "Port" in line:
      a += line
    if "Status" in line:
      line = line[9:]
      if(line[0] != ' ' and line.split()[2][0] != '4' and line.split()[2][0] != '5'):
        a += line.split()[0] + "\n"

if(a == ""):
  for key, value in ps.items():
    if(value == "http" or value == "https"):  
      a += "Port " + key + " (" + value + ") -\n"

a = a.strip()
a = a.split("\n")
      
for dir in a:
  if("Port" in dir):
    b += dir
    key = dir.split()[1]
    value = dir.split()[2][1:-1]
    subprocess.call(['bash', './curl.sh', ip, key, value, ""])
  else:
    b += dir
    subprocess.call(['bash', './curl.sh', ip, key, value, dir])
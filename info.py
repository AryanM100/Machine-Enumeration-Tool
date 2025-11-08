#!/bin/python3

import sys
import ast

ip = sys.argv[1]
ps = sys.argv[2]
ps = ast.literal_eval(ps)
ports = list(ps.keys())
service = list(ps.values())

linux = "linux"
windows = "windows"
solaris = "solaris"
freebsd = "freebsd"
osx = "osx"
osx2 = "os x"
a = ""
b = ""
c = ""
e = ""
hosts = ""

with open('Text/nmap') as f:
  for line in f:
    if linux in line.lower() or windows in line.lower() or solaris in line.lower() or freebsd in line.lower() or osx in line.lower() or osx2 in line.lower():
      if linux in line.lower():
        a = linux
      if windows in line.lower():
        a = windows
      if solaris in line.lower():
        a = solaris
      if freebsd in line.lower():
        a = freebsd
      if  osx in line.lower():
        a = osx
      if osx2 in line.lower():
        a = osx2

if '53' in ports:
  with open('Text/dns') as f:
    for line in f:
      if "PTR" in line:
        b = line.split()
        c = ip + " " +  b[2]
        with open('/etc/hosts', 'r') as file:
          hosts = file.readlines()
        
        if c+'\n' not in hosts:
          d = hosts.index('\n')
          hosts.insert(d, c+'\n')

          with open('/etc/hosts', 'w') as file:
            file.writelines(hosts)

if '139' in ports or '445' in ports:
  with open('Text/smbversion') as f:
    for line in f:
      if ip+":139" in line:
        e = line.split()
        e = e[-2] + " " + e[-1]
        e = e.replace("(", "")
        e = e.replace(")", "")
        e = e[:-3]

with open('Text/info', 'w') as f:
  f.write(a+" "+e)
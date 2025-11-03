#!/bin/python3

import argparse
import subprocess
import ast

parser = argparse.ArgumentParser(description = "This is a Machine Exploitation Tool which will tell you the exploit you need to run in order to gain access to the machine, if it has an exploit.")
parser.add_argument("-i", metavar="",help="Provide an IP", type=str)
args = parser.parse_args()

ip = args.i
result = ""
ports = []
service = []
ps = {}
w = ""
v = ""
r = ""
s = ""

if(ip == None):
  print("Use this tool with an option. Use -h or --help for help.")

elif(ip != None):
  octet = ip.split(".")
  for i in range(0, len(octet)):
    if(not(octet[i].isdigit()) or int(octet[i]) < 0 or int(octet[i]) > 255 or len(octet) != 4):
      print("Provide a valid IP address.")
      break
  
  subprocess.call(['bash', './ports.sh', ip])

  with open('Text/ports') as file:
    for line in file:
      if(line[0].isdigit() and "/" in line):
        line = line.split()
        s += line[0].split("/")[0] + ","
  
  s = s[0:-1]

  subprocess.call(['bash', './nmap.sh', ip, s])
  
  output = subprocess.run(['python3', 'ver.py'], text=True, capture_output=True)
  ps = output.stdout.strip()

  ps = ast.literal_eval(ps)
  ports = list(ps.keys())
  service = list(ps.values())

  print("Ports open on this machine -")
  print(ps)
  print("Nmap result has been saved.")
  print("---------------------------------------------------------------------------------------------------------------------------------")

  if 'http' in service or 'https' in service:
    print("Run ffuf ?")
    a = input()
    if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"):
      for key, value in ps.items():
        if(value == "http" or value == "https"):
          subprocess.call(['bash', './ffuf.sh', ip, key, value])
        
          with open('Text/ffuf') as f:
            print("Port " + key + " (" + value + ") -")
            for line in f:
              if "Status" in line and "#" not in line:
                print(line, end='')
            print()

    print("---------------------------------------------------------------------------------------------------------------------------------")

  if '21' in ports:
    print("FTP -")
    subprocess.call(['bash', './ftp.sh', ip])

    with open('Text/ftp') as f:
      for line in f:
        if "incorrect" in line:
          print("Anonymous Login Failed.")
    print("---------------------------------------------------------------------------------------------------------------------------------")

  if '139' in ports or '445' in ports:
    with open('Text/inputmsf', 'w') as f:
      f.write("""use auxiliary/scanner/smb/smb_version
set RHOSTS """)
      f.write(ip)
      f.write("\nrun")

    subprocess.call(['bash', './smb.sh', ip])

    print("smbclient -")

    with open("Text/smb") as f:
      for line in f:
        if "Anonymous" in line:
          print(line)
        if "Sharename" in line:
          print(line, end='')
          for line in f:
            print(line, end='')

    print("---------------------------------------------------------------------------------------------------------------------------------")

    print("msfconsole smb_version -")

    with open("Text/smbversion") as f:
      for line in f:
        if ip+":139" in line:
          print(line, end='')
          for line in f:
            if "stty" in line:
              break
            print(line, end='')

    print("---------------------------------------------------------------------------------------------------------------------------------")

  if '2049' in ports:
    print("NFS -")
    subprocess.call(['bash', './nfs.sh', ip])
    with open('Text/nfs') as f:
      for line in f:
        if "Export" not in line and line.strip() != "":
          w = line.split()
          w = w[0]
          print("NFS Share present so it is extracted, check /mnt/vms.")
          subprocess.call(['bash', './nfs2.sh', ip, w])
    print("---------------------------------------------------------------------------------------------------------------------------------")


  if '53' in ports:
    print("DNSRecon -")
    subprocess.call(['bash', './dns.sh', ip])
    print("---------------------------------------------------------------------------------------------------------------------------------")
  
  if 'ssh' in ps.values() or 'smtp' in ps.values() or 'pop3' in ps.values() or 'ftp' in ps.values():
    print("Use Hydra to bruteforce ? If yes provide username and port separated by a space, or say no(n).")
    a = input()

    if(a != "N" and a != "n" and a != "no" and a != "No" and a != "NO"):
      u, p = a.split()
      s = ps[p]
      subprocess.call(['bash', './hydra.sh', ip, u, p, s])

      with open('Text/hydra') as f:
        for line in f:
          if "host" in line:
            print(line, end='')
            for line in f:
              if "github" not in line:
                print(line, end='')

    print("---------------------------------------------------------------------------------------------------------------------------------")

  subprocess.call(['python3', 'info.py', ip, str(ports)])

  with open('Text/info') as f:
    for line in f:
      v += line + " "
      with open('Text/inputexploit', 'w') as file:
        file.write("search " + v)
  
  if(len(v.split()) > 1):
    subprocess.call(['bash', './exploit.sh', ip])

    print("Exploits -")

    with open("Text/exploit") as f:
      for line in f:
        if "Matching Modules" in line:
          print(line, end='')
          for line in f:
            if "stty" in line:
              break
            if "For example" in line:
              break
            print(line, end='')

  with open("Text/results", 'w') as f:
    f.write(r)
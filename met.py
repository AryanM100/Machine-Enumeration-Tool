#!/bin/python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description = "This is a Machine Exploitation Tool which will tell you the exploit you need to run in order to gain root access to the machine, if it has an exploit.")
parser.add_argument("-i", metavar="",help="Provide an IP", type=str)
args = parser.parse_args()

ip = args.i
result = ""
ports = []
x = ""
y = ""
z = ""
w = ""
v = ""
#/home/ryan/HackinStuff/IS/MET/

if(ip == None):
  print("Use this tool with an option. Use -h or --help for help.")

elif(ip != None):
  octet = ip.split(".")
  for i in range(0, len(octet)):
    if(not(octet[i].isdigit()) or int(octet[i]) < 0 or int(octet[i]) > 255 or len(octet) != 4):
      print("Provide a valid IP address.")
      break
  
  #subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./nmap.sh', ip])
  
  output = subprocess.run(['python3', '/home/ryan/HackinStuff/IS/MET/ver.py'], text=True, capture_output=True)
  ports = output.stdout.strip()

  print("Ports open on this machine -")
  print(ports)
  print("Nmap result has been saved.")
  print("---------------------------------------------------------------------------------------------------------------------------------")

  if '80' in ports or '443' in ports or '8080' in ports:
    if '80' in ports:
      x = "80"
    if '443' in ports:
      y = "443"
    if '8080' in ports:
      z = "8080"
    print("Run ffuf ?")
    a = input()
    if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"):
      subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./ffuf.sh', ip, x, y, z])

      if '80' in ports:
        print("Port 80 -")

        with open('/home/ryan/HackinStuff/IS/MET/ffuf1') as f:
          for line in f:
            if "Status" in line and "#" not in line:
              print(line, end='')

      if '443' in ports:

        print("Port 443 -")

        with open('/home/ryan/HackinStuff/IS/MET/ffuf2') as f:
          for line in f:
            if "Status" in line and "#" not in line:
              print(line, end='')

      if '8080' in ports:

        print("Port 8080 -")

        with open('/home/ryan/HackinStuff/IS/MET/ffuf3') as f:
          for line in f:
            if "Status" in line and "#" not in line:
              print(line, end='')

    print("---------------------------------------------------------------------------------------------------------------------------------")

  if '21' in ports:
    print("FTP -")
    subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./ftp.sh', ip])

    with open('/home/ryan/HackinStuff/IS/MET/ftp') as f:
      for line in f:
        if "incorrect" in line:
          print("Anonymous Login Failed.")
    print("---------------------------------------------------------------------------------------------------------------------------------")

  if '22' in ports:
    print("Bruteforce SSH ? If yes provide username, or say no(n).")
    a = input()
    if(a != "N" and a != "n" and a != "no" and a != "No" and a != "NO"):
      subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./ssh.sh', ip, a])

      with open('/home/ryan/HackinStuff/IS/MET/hydra') as f:
        for line in f:
          if "host" in line:
            print(line, end='')
            for line in f:
              if "github" not in line:
                print(line, end='')

    print("---------------------------------------------------------------------------------------------------------------------------------")

  if '139' in ports or '445' in ports:
    with open('/home/ryan/HackinStuff/IS/MET/inputmsf', 'w') as f:
      f.write("""use auxiliary/scanner/smb/smb_version
set RHOSTS """)
      f.write(ip)
      f.write("\nrun")

    subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./smb.sh', ip])

    print("smbclient -")

    with open("/home/ryan/HackinStuff/IS/MET/smb") as f:
      for line in f:
        if "Anonymous" in line:
          print(line)
        if "Sharename" in line:
          print(line, end='')
          for line in f:
            print(line, end='')

    print("---------------------------------------------------------------------------------------------------------------------------------")

    print("msfconsole smb_version -")

    with open("/home/ryan/HackinStuff/IS/MET/smbversion") as f:
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
    subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./nfs.sh', ip])
    with open('nfs') as f:
      for line in f:
        if "Export" not in line and line.strip() != "":
          w = line.split()
          w = w[0]
          print("NFS Share present so it is extracted, check /mnt/vms.")
          subprocess.call(['bash', './nfs2.sh', ip, w])
    print("---------------------------------------------------------------------------------------------------------------------------------")


  if '53' in ports:
    print("DNSRecon -")
    subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./dns.sh', ip])
    print("---------------------------------------------------------------------------------------------------------------------------------")


  subprocess.call(['python3', 'info.py', ip, ports])

  with open('info') as f:
    for line in f:
      v += line + " "
      with open('inputexploit', 'w') as file:
        file.write("search " + v)
  
  subprocess.call(['bash', '/home/ryan/HackinStuff/IS/MET/./exploit.sh', ip])

  print("Exploits -")

  with open("/home/ryan/HackinStuff/IS/MET/exploit") as f:
    for line in f:
      if "Matching Modules" in line:
        print(line, end='')
        for line in f:
          if "stty" in line:
            break
          if "For example" in line:
            break
          print(line, end='')
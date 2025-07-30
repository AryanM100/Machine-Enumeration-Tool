#!/bin/bash

ip=$(echo $1)
a="smb_version"

smbclient -L \\\\$ip\\ > /home/ryan/HackinStuff/IS/MET/smb < /home/ryan/HackinStuff/IS/MET/inputsmb 2>&1

msfconsole > /home/ryan/HackinStuff/IS/MET/smbversion < /home/ryan/HackinStuff/IS/MET/inputmsf 2>&1
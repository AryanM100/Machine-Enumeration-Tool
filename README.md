# Machine-Enumeration-Tool

A tool to automate the initial enumeration steps for penetration testing boxes like Kioptrix or rooms on TryHackMe.

## Prerequisites

*   Python 3.x
*   Nmap
*   NFS common tools (`nfs-common`)
*   ffuf
*   hydra
*   smbclient
*   dnsrecon
*   ftp
*   Metasploit (`msfconsole`)

On Debian-based systems, you can install most of them with:
```bash
sudo apt update && sudo apt install nmap nfs-common ffuf hydra smbclient dnsrecon ftp
```

## Installation

```bash
git clone https://github.com/AryanM100/Machine-Enumeration-Tool.git
cd Machine-Enumeration-Tool
```

## Usage

**Important: Run the script as a normal user. Do not use sudo to run met.py directly.**

The script is creating files in `Text/` directory and if you use sudo they will be owned by root and can cause issues.
It will automatically prompt you for your password when it needs to perform a task that requires root permissions.

```bash
python3 met.py -i "IP_ADDRESS"
```

### Why Root is Required

This tool needs root perms for the following commands -
```bash
nmap -p- --open -sS --min-rate 5000 -Pn -n $ip (`ports.sh`)

mkdir /mnt/vms (`nfs2.sh`)

mount -t nfs $ip:$w /mnt/vms (`nfs2.sh`)
```
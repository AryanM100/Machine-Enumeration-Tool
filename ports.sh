#!/bin/bash

ip=$(echo $1)

sudo nmap -p- --open -sS --min-rate 5000 -Pn -n $ip > Text/ports
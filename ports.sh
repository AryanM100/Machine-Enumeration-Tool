#!/bin/bash

ip=$(echo $1)

d="Text"

if [ -d "$d" ]; then
  true
else
  mkdir Text
fi

sudo nmap -p- --open -sS --min-rate 5000 -Pn -n $ip > Text/ports
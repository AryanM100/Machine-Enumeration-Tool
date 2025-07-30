#!/bin/bash

ip=$(echo $1)
x=$(echo $2)
y=$(echo $3)
z=$(echo $4)

if [[ "$x" == "80" ]]; then
   ffuf -w /home/ryan/HackinStuff/HelpThings/dlistmedium.txt -u http://$ip/FUZZ > ffuf1 2>&1
fi

if [[ "$y" == "443" ]]; then
   ffuf -w /home/ryan/HackinStuff/HelpThings/dlistmedium.txt -u https://$ip/FUZZ > ffuf2 2>&1
fi

if [[ "$z" == "8080" ]]; then
   ffuf -w /home/ryan/HackinStuff/HelpThings/dlistmedium.txt -u http://$ip:8080/FUZZ > ffuf3 2>&1
fi
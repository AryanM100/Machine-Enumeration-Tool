#!/bin/bash

ip=$(echo $1)
port=$(echo $2)
service=$(echo $3)

ffuf -c -w Wordlists/dlistmedium.txt -u $service://$ip:$port/FUZZ > Text/ffuf 2>&1
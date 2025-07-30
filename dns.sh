#!/bin/bash

ip=$(echo $1)

dnsrecon -r 127.0.0.0/24 -n $ip -d random | tee /home/ryan/HackinStuff/IS/MET/dns
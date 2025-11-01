#!/bin/bash

ip=$(echo $1)
username=$(echo $2)
port=$(echo $3)
service=$(echo $4)

hydra -l $username -P Wordlists/fasttrack.txt $ip -s $port $service -V > Text/hydra 2>&1
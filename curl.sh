#!/bin/bash

ip=$(echo $1)
port=$(echo $2)
service=$(echo $3)
dir=$(echo $4)

echo $service://$ip:$port/$dir >> Text/curl.txt
curl -L $service://$ip:$port/$dir >> Text/curl.txt 2>&1
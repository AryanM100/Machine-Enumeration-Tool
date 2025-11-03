#!/bin/bash

ip=$(echo $1)
w=$(echo $2)

d="/mnt/vms"

if [ -d "$d" ]; then
  true
else
  mkdir /mnt/vms
fi

mount -t nfs $ip:$w /mnt/vms
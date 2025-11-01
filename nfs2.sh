#!/bin/bash

ip=$(echo $1)
w=$(echo $2)

mkdir /mnt/vms
mount -t nfs $ip:$w /mnt/vms
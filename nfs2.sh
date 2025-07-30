#!/bin/bash

ip=$(echo $1)
w=$(echo $2)

mount -t nfs $ip:$w /mnt/vms
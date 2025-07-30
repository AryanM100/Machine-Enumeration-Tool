#!/bin/bash

ip=$(echo $1)

showmount -e $ip | tee nfs
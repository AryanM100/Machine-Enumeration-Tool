#!/bin/bash

ip=$(echo $1)

ftp ftp://anonymous:anonymous@$ip 2>/dev/null | tee Text/ftp
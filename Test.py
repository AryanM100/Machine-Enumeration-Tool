#!/bin/python3

with open('nfs') as f:
  for line in f:
    if "Export" not in line:
      w = line.split()
      w = w[0]
      print("1")
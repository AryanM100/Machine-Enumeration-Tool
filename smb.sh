#!/bin/bash

ip=$(echo $1)
a="smb_version"

smbclient -L \\\\$ip\\ > Text/smb < Text/inputsmb 2>&1

msfconsole > Text/smbversion < Text/inputmsf 2>&1
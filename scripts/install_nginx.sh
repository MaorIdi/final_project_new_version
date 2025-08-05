#!/bin/bash
#
#   This script is installing nginx on a machine isntance based on its name.
#

vm_name=$1

if [[ ! -z $vm_name ]]; then
    echo "Installing nginx on $vm_name..."
    sleep 2
    echo "Installation successful."
else
    echo "Please pass vm_name as an argument."
    exit 1
fi

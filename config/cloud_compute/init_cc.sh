!#/bin/bash

# Verify Virtualization is switched on
lscpu | grep Virtualization

# Install qemu
apt-get install qemu-system

# 

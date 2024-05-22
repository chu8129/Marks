#!/bin/sh
#wget https://us.download.nvidia.com/XFree86/Linux-x86_64/535.146.02/NVIDIA-Linux-x86_64-535.146.02.run
sudo apt install build-essential libglvnd-dev pkg-config
sudo apt autoremove
sudo systemctl stop gdm.service
sudo systemctl disable gdm.service
sudo systemctl status gmd.service
sudo systemctl set-default multi-user.target
sudo service lightdm stop
sudo service docker stop
sudo rmmod nvidia_uvm
sudo service nvidia-persistenced stop

#wget https://us.download.nvidia.com/XFree86/Linux-x86_64/550.78/NVIDIA-Linux-x86_64-550.78.run
sudo apt install build-essential libglvnd-dev pkg-config
filename=./NVIDIA-Linux-x86_64-535.146.02.run
chmod +x ${filename}
sudo ${filename}

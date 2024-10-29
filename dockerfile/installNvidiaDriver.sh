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


# method 
apt-get install nvidia-driver-515
apt-get install nvidia-driver-550


# ucloud
sudo apt-get update
sudo systemctl stop apt-daily.service
sudo systemctl stop apt-daily.timer
sudo systemctl stop apt-daily-upgrade.service
sudo systemctl stop apt-daily-upgrade.timer
sudo systemctl disable apt-daily.service
sudo systemctl disable apt-daily.timer
sudo systemctl disable apt-daily-upgrade.service
sudo systemctl disable apt-daily-upgrade.timer
sudo apt-mark hold linux-image-generic linux-headers-generic linux-image-$(uname -r) linux-headers-$(uname -r)
apt-mark showhold


sudo apt-get install libfuse2 libnl-3-dev libnl-route-3-dev tk -y
sudo apt-get install gfortran libgfortran5 bison libnl-route-3-200 flex -y
sudo apt-get install make net-tools unzip -y
sudo wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb

os_version=ubuntu2204
cuda_version=12.2.2
driver_version=535.104.05
nccl_version=2.18.5
driver_main_version=$(echo $driver_version | awk -F '.' '{print $1}')
base_developer_url=https://developer.download.nvidia.cn/compute
cuda_main_version=${cuda_version:0:4}
cuda_download_url=${base_developer_url}/cuda/${cuda_version}/local_installers/cuda_${cuda_version}_${driver_version}_linux.run
nccl_download_url=${base_developer_url}/cuda/repos/${os_version}/x86_64/libnccl2_${nccl_version}-1+cuda${cuda_main_version}_amd64.deb
nccl_dev_download_url=${base_developer_url}/cuda/repos/${os_version}/x86_64/libnccl-dev_${nccl_version}-1+cuda${cuda_main_version}_amd64.deb

wget $nccl_download_url
wget $nccl_dev_download_url
wget $cuda_download_url


cat >> /etc/modprobe.d/blacklist-nouveau.conf << EOF
blacklist nouveau
options nouveau modeset=0
EOF


sudo update-initramfs -u

rmmod nouveau
sudo sh cuda_${cuda_version}_${driver_version}_linux.run --silent --driver --toolkit
sudo dpkg -i libncc*.deb


cat >> ~/.bashrc << EOF
export LD_LIBRARY_PATH=/usr/local/cuda/lib64
export PATH=$PATH:/usr/local/cuda/bin
EOF
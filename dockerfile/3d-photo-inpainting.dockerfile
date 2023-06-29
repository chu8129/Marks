# https://github.com/vt-vl-lab/3d-photo-inpainting.git # 

# build cache 支持:DOCKER_BUILDKIT=1 docker build ***
from nvidia/cuda:11.6.1-cudnn8-devel-ubuntu20.04

run sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
run sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list
RUN apt update


run ln -snf /usr/share/zoneinfo/$(curl https://ipapi.co/timezone) /etc/localtime
ENV DISPLAY=:0
ENV CUDA_VISIBLE_DEVICES=0
RUN apt install -y --fix-missing libfontconfig1-dev wget ffmpeg libsm6 libxext6 libxrender-dev mesa-utils-extra libegl1-mesa-dev libgles2-mesa-dev xvfb


run apt-get install -y python3-pip
run pip config set global.index-url https://pypi.douban.com/simple/
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U numpy==1.23.1
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U vispy==0.6.4
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U moviepy==1.0.2
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U transforms3d==0.3.1
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U networkx==2.3
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U Cython
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U cynetworkx
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U opencv-python==4.2.0.32
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U scipy matplotlib scikit-image
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U pyyaml
run pip install torchvision==0.13.0+cu116 torchaudio==0.12.0+cu116 --extra-index-url https://download.pytorch.org/whl/cu116



COPY . /app/
WORKDIR /app


# #!/bin/sh
# export DISPLAY=:1
# Xvfb :1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &
# python3 -c "import vispy; print(vispy.sys_info())"
# python3 main.py --config argument.yml

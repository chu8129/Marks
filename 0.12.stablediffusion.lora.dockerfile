
# 系统环境配置
# build cache 支持:DOCKER_BUILDKIT=1 docker build ***

from nvidia/cuda:11.6.1-cudnn8-devel-ubuntu20.04

run sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
run sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list
run apt install --fix-broken && apt update && apt upgrade -y
run apt install -y wget 
run apt install -y gcc build-essential


# conda
ENV CONDA_DIR /opt/conda/
ARG CONDA_ENV=env
run wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh 
run /bin/bash /miniconda.sh -b -p $CONDA_DIR
ENV PATH $CONDA_DIR/bin:$PATH
run conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
run conda create --name ${CONDA_ENV} python=3.10.9=h7a1cb2a_0
ENV PATH $CONDA_DIR/envs/${CONDA_ENV}/bin:$PATH
run python -V > /python.version

# tf
# run wget https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-2.10.0.tar.gz
# run tar -C /usr/local -xzf libtensorflow-gpu-linux-x86_64-2.10.0.tar.gz
# run ldconfig
# run rm libtensorflow-gpu-linux-x86_64-2.10.0.tar.gz


# 设置时区
run apt install -y curl
run ln -snf /usr/share/zoneinfo/$(curl https://ipapi.co/timezone) /etc/localtime

run apt update && apt install -y python3-pip python3-opencv cmake vim git vim ffmpeg --fix-missing
run python -V
run pip -h

# python相关
# run ln -s $(which python3) /usr/local/bin/python
# run ln -s $(which pip3) /usr/bin/pip

# 缺少libGL文件:opencv:2
# ImportError: libGL.so.1: cannot open shared object file: No such file or directory
run apt install -y libgl1-mesa-glx
run apt install -y 	libegl1
# ImportError: ('Unable to load OpenGL library', 'OSMesa: cannot open shared object file: No such file or directory', 'OSMesa', None)
run apt install -y libosmesa6-dev
# opencv
# ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory
run apt install -y libglib2.0-dev
# ImportError: libSM.so.6: cannot open shared object file: No such file or directory
# ImportError: libXrender.so.1: cannot open shared object file: No such file or directory
# ImportError: libXext.so.6: cannot open shared object file: No such file or directory
run apt install -y libsm6 libxrender-dev libxext6

# pip配置
run pip config set global.index-url https://pypi.douban.com/simple/
run python -m pip install --upgrade pip


run pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116

copy condareq.yaml /condareq.yaml
copy pipreq.txt /pipreq.txt
run conda env update -f /condareq.yaml
run apt install -y libcairo2-dev
run pip3 install git+https://github.com/pygobject/pycairo.git

run mkdir /.local && chmod +777 /.local
run mkdir /.config && chmod +777 /.config
run mkdir /.cache && chmod +777 /.cache

# run pip3 install -f /pipreq.txt

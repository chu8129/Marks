
# 系统环境配置
# build cache 支持:DOCKER_BUILDKIT=1 docker build ***

# from nvidia/cuda:11.6.2-cudnn8-runtime-ubuntu20.04
# from nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04
from nvidia/cuda:12.0.0-cudnn8-devel-ubuntu22.04

ENV LANG C.UTF-8

run sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
run sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list
run apt autoremove
run apt update
run apt-get install -y --no-install-recommends wget build-essential zip unzip unzip openssh-client


# conda
ENV CONDA_DIR /opt/conda/
ARG CONDA_ENV=env
run wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh 
run /bin/bash /miniconda.sh -b -p $CONDA_DIR
ENV PATH $CONDA_DIR/bin:$PATH
run conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
run conda create --name ${CONDA_ENV} python=3.11
ENV PATH $CONDA_DIR/envs/${CONDA_ENV}/bin:$PATH
run python -V > /python.version

# tf
# run wget https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-2.10.0.tar.gz
# run tar -C /usr/local -xzf libtensorflow-gpu-linux-x86_64-2.10.0.tar.gz
# run ldconfig
# run rm libtensorflow-gpu-linux-x86_64-2.10.0.tar.gz


# 设置时区
run apt update && apt install -y --no-install-recommends --fix-missing curl
# run ln -s /usr/share/zoneinfo/$(curl https://ipapi.co/timezone) /etc/localtime
run ln -s /usr/share/zoneinfo/Asia/Chongqing /etc/localtime

ENV TZ Asia/Chongqing
run echo $TZ > /etc/timezone

ENV DEBIAN_FRONTEND noninteractive
run apt update

run apt install -y --no-install-recommends --fix-missing software-properties-common 
run add-apt-repository --yes --update ppa:ansible/ansible
run apt update && apt install -y --no-install-recommends python3-pip python3-opencv cmake vim git vim ffmpeg ansible --fix-missing

# python相关
# run ln -s $(which python3) /usr/local/bin/python
# run ln -s $(which pip3) /usr/bin/pip

# 缺少libGL文件:opencv:2
# ImportError: libGL.so.1: cannot open shared object file: No such file or directory
run apt install -y --no-install-recommends libgl1-mesa-glx
run apt install -y --no-install-recommends libegl1
# ImportError: ('Unable to load OpenGL library', 'OSMesa: cannot open shared object file: No such file or directory', 'OSMesa', None)
run apt install -y --no-install-recommends libosmesa6-dev
# opencv ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory
run apt install -y --no-install-recommends libglib2.0-dev
# ImportError: libSM.so.6: cannot open shared object file: No such file or directory
# ImportError: libXrender.so.1: cannot open shared object file: No such file or directory
# ImportError: libXext.so.6: cannot open shared object file: No such file or directory
run apt install -y --no-install-recommends libsm6 libxrender-dev libxext6

# pip配置
run pip config set global.index-url https://pypi.douban.com/simple/
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip python -m pip install --upgrade pip
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pysocks
# 模型框架优先
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install tensorflow
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install torch_scatter torch_sparse torch_cluster torch-geometric --extra-index-url https://download.pytorch.org/whl/cu116
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install onnx==1.13.0 onnxruntime-gpu==1.13.1 onnxconverter-common==1.13.0
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install onnx onnxruntime-gpu onnxconverter-common
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install xgboost
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/facebookresearch/fastText.git
# 框架扩展
# torch
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0+cu116 --extra-index-url https://download.pytorch.org/whl/cu116
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install torch-geometric==2.1.0.post1
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install torch-scatter==2.1.0
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install torch-sparse==0.6.15
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/Lightning-AI/lightning.git -i https://pypi.python.org/simple/
# onnx
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install tf2onnx===1.13.0 keras2onnx
# tensorflow
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install tensorflow-addons tensorflow_hub
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install tensorflow_decision_forests
# 综合
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install bitsandbytes
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install safetensors
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/huggingface/datasets.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/huggingface/evaluate.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/huggingface/accelerate.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/huggingface/diffusers.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -U tokenizers
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/huggingface/transformers.git@v4.35.2
# CV
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install openmesh
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/scikit-image/scikit-image.git
# -i https://pypi.python.org/simple/
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/CalciferZh/vctoolkit.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/albumentations-team/albumentations.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/facebookresearch/fvcore.git
# 服务工具
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install Flask zerorpc gunicorn requests
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pymysql elasticsearch
# 便捷工具
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install tqdm fire
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install absl-py
# 格式化工具
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install flake8 black isort pylint
# 代码工具
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install jupyter jupyterlab pydot
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install matplotlib seaborn
# 模型展示
run apt install -y --no-install-recommends graphviz
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pytest
# 数据工具
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install opencv-python #-headless
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pandas
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install scikit-learn==0.24.2
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/scikit-learn/scikit-learn.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pyahocorasick==1.4.2
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install jieba==0.42.1
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install synonyms==3.16.0
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install textda==0.1.0.6
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install nlpcda==2.5.8
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install numpy

# gesture
run apt install -y --no-install-recommends protobuf-compiler
run apt install -y --no-install-recommends apt-transport-https curl gnupg
run curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg && mv bazel.gpg /etc/apt/trusted.gpg.d/ 
run echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
run apt update && apt install -y --no-install-recommends bazel
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install mediapipe
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/google/mediapipe.git
# music
run apt install -y --no-install-recommends timidity libsndfile1
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pydub librosa music21 dtw-python
# wav2vec2
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip3 install -q git+https://github.com/vasudevgupta7/gsoc-wav2vec2@main
# joint ContactPose
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install trimesh pyrender pyopengl==3.1.5 chumpy
# nanodet
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pycocotools
# stable diffusion
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/XPixelGroup/BasicSR.git  -i https://pypi.python.org/simple/
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install gfpgan
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install gradio
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install piexif
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install olefile # olefile->PIL.Image
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install oss2
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install git+https://github.com/xinntao/Real-ESRGAN.git
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install moviepy
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install ninja
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -v -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers
# TTS
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install unidecode jamo cn2an pypinyin
# run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pyopenjtalk==0.2.0
# microsoft
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install sentencepiece
# fastspeech2
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install fairseq g2p_en
run python -c "import nltk; nltk.download('all')"
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install tensorboardX
# balacoon-tts
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install balacoon-tts -i https://pypi.fury.io/balacoon/
# 3d-photo-inpainting
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install sk-video
# imagemagick
run apt install -y --no-install-recommends imagemagick
# dlib
run pip install dlib -U
# viu
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN . "$HOME/.cargo/env" && cargo install viu
# extra 
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install segment-anything
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install pytorch-fid
run --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install ultralytics
run python -c "import ultralytics;import inspect;import os; os.system(f'sed -i \'/CUBLAS_WORKSPACE_CONFIG/d\' {inspect.getsourcefile(ultralytics.utils)}')"
run python -c "import ultralytics;import inspect;import os; os.system(f'sed -i \'/CUBLAS_WORKSPACE_CONFIG/d\' {inspect.getsourcefile(ultralytics.utils.torch_utils)}')"
run python -c "import ultralytics;import inspect;import os; os.system(f'sed -i \'/torch.backends.cudnn.deterministic/d\' {inspect.getsourcefile(ultralytics.utils.torch_utils)}')"
run python -c "import ultralytics;import inspect;import os; os.system(f'sed -i \'/torch.use_deterministic_algorithms/d\' {inspect.getsourcefile(ultralytics.utils.torch_utils)}')"

# docsify
run curl -sL https://deb.nodesource.com/setup_19.x | bash -
run apt install -y nodejs && echo "Node: " && node -v && echo "NPM: " && npm -v
run npm install docsify-cli -g && npm list -g | grep docsify


# 缓存
# [Synonyms] downloading data from 
# https://github.com/chatopera/Synonyms/releases/download/3.15.0/words.vector.gz to /usr/local/lib/python3.8/dist-packages/synonyms/data/words.vector.gz ... 
# run mkdir -p /usr/local/lib/python3.8/dist-packages/synonyms/data/ && wget https://github.com/chatopera/Synonyms/releases/download/3.15.0/words.vector.gz -o  /usr/local/lib/python3.8/dist-packages/synonyms/data/words.vector.gz
copy words.vector.gz /usr/local/lib/python3.8/dist-packages/synonyms/data/words.vector.gz


# clean,使用缓存挂载了系统的就不要清理
run conda clean --all
run rm /miniconda.sh
run pip cache purge
run apt clean && apt-get clean && rm -rf /var/lib/apt/lists/*
run bash -ic 'history -c'
run echo "" > ~/.bash_history

# mount
run alias ls='ls $LS_OPTIONS'
run export LANG=C.UTF-8
run git config --global user.email "chu8129@gmail.com"
run git config --global user.name "wangqiuwen"

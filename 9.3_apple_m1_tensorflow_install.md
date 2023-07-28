```
wget:https://github.com/conda-forge/miniforge***

安装miniforge3
chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh
sh ~/Downloads/Miniforge3-MacOSX-arm64.sh
source ~/miniforge3/bin/activate

一堆依赖和安装
conda install -c apple tensorflow-deps
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal


取消自动进入conda基础环境
conda config --set auto_activate_base false
```

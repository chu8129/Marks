### 错误1
```
*** 
    import paddlehub as hub
  File "/usr/local/lib/python3.6/site-packages/paddlehub/__init__.py", line 18, in <module>
    import paddle
  File "/usr/local/lib/python3.6/site-packages/paddle/__init__.py", line 28, in <module>
    batch = batch.batch
NameError: name 'batch' is not defined
```
```
docker run -it dm:v5 cat /usr/local/lib/python3.6/site-packages/paddle/__init__.py|grep batch
import paddle.batch
batch = batch.batch

docker run -it dm:v5 pip freeze|grep paddle
paddle2onnx==0.5.1
paddlehub==2.1.0
paddlenlp==2.0.0rc18
paddlepaddle==2.0.2

额？？？只能build docker时replace打补丁了
```
### Dockerfile,历史版本各种坑加了目录，还有可能少了so加了apt install，还有cv2的安装问题，python -c是为了一次性下载
```
FROM python:3.6
RUN python -m pip install --upgrade pip

ADD requirements.txt .

RUN mkdir -p /root/.cache
RUN mkdir -p /.cache/paddle
RUN mkdir -p /root/.pylint.d
RUN mkdir -p /root/.paddlehub/modules/lac

RUN apt update
RUN apt install -fy ffmpeg libsm6 libxext6
RUN python -m pip install opencv-python-headless==4.5.1.48 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
RUN python -m pip install paddlepaddle==2.0.2 -i https://mirror.baidu.com/pypi/simple
RUN python -m pip install paddlehub==2.1.0 -i https://mirror.baidu.com/pypi/simple

RUN sed -i "s/import paddle.batch/from import import batch/g" /usr/local/lib/python3.6/site-packages/paddle/__init__.py
RUN sed -i "s/batch = batch.batch/batch = paddle.batch.batch/g" /usr/local/lib/python3.6/site-packages/paddle/__init__.py
RUN python -c "import paddlehub as hub;print(hub.Module(name='lac').lexical_analysis(data={'text':['我是个测试机器人']}))"
```
### 错误2
```
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.6/site-packages/paddlehub/__init__.py", line 18, in <module>
    import paddle
  File "/usr/local/lib/python3.6/site-packages/paddle/__init__.py", line 29, in <module>
    from .fluid import monkey_patch_variable
  File "/usr/local/lib/python3.6/site-packages/paddle/fluid/__init__.py", line 51, in <module>
    from . import io
  File "/usr/local/lib/python3.6/site-packages/paddle/fluid/io.py", line 40, in <module>
    from . import reader
  File "/usr/local/lib/python3.6/site-packages/paddle/fluid/reader.py", line 25, in <module>
    from .dataloader import BatchSampler, Dataset, IterableDataset
  File "/usr/local/lib/python3.6/site-packages/paddle/fluid/dataloader/__init__.py", line 17, in <module>
    from . import dataset
  File "/usr/local/lib/python3.6/site-packages/paddle/fluid/dataloader/dataset.py", line 18, in <module>
    import paddle.dataset.common
  File "/usr/local/lib/python3.6/site-packages/paddle/dataset/__init__.py", line 18, in <module>
    import paddle.dataset.mnist
  File "/usr/local/lib/python3.6/site-packages/paddle/dataset/mnist.py", line 23, in <module>
    import paddle.dataset.common
  File "/usr/local/lib/python3.6/site-packages/paddle/dataset/common.py", line 55, in <module>
    must_mkdirs(DATA_HOME)
  File "/usr/local/lib/python3.6/site-packages/paddle/dataset/common.py", line 48, in must_mkdirs
    os.makedirs(DATA_HOME)
  File "/usr/local/lib/python3.6/os.py", line 220, in makedirs
    mkdir(name, mode)
PermissionError: [Errno 13] Permission denied: '/.cache/paddle/dataset'
```
### 问题：为何这么奇怪的路径,可能是docker问题，更新了版本解决

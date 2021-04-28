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

哪个实习生写的？？？只能build docker时replace打补丁了
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

RUN sed -i "s/batch = batch.batch/batch = paddle.batch.batch/g" /usr/local/lib/python3.6/site-packages/paddle/__init__.py
RUN python -c "import paddlehub as hub;print(hub.Module(name='lac').lexical_analysis(data={'text':['我是个测试机器人']}))"
```

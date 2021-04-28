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

只能build docker时replace
```

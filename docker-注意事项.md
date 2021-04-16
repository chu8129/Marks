```
如果机器开了swap记得加上
run --rm -m 1536m  --memory-swap 2048m
```

### 日常使用(如果有必要，time)
```
docker run -e TZ=Asia/Shanghai --log-opt max-size=5m --log-opt max-file=1 --user 1001:1001 --rm -m 500m --memory-swap 2048m -v path:path  --name feed_aweme_%(process_num)02d -e LOG_LEVEL=DEBUG -e CONSUL=consul:// dm:v0 python -m apps***
```

```
docker -t build dm:v3 .
```

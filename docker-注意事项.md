```
如果机器开了swap记得加上
run --rm -m 1536m  --memory-swap 2048m
```

```
docker run -e TZ=Asia/Shanghai --log-opt max-size=5m --log-opt max-file=1 --user 1001:1001 --rm -m 500m --memory-swap 2048m -v path:path  --name feed_aweme_%(process_num)02d dm:v0 python -m apps***
```

```
docker -t build dm:v3 .
```

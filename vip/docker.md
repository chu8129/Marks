```
docker run -d -p 8051:8050 --memory=3G --restart=always scrapinghub/splash:master --maxrss 2048 --disable-browser-caches 
docker run -d -p 8052:8050 --memory=3G --restart=always scrapinghub/splash:master --maxrss 2048 --disable-browser-caches 
docker run -d -p 8053:8050 --memory=3G --restart=always scrapinghub/splash:master --maxrss 2048 --disable-browser-caches 
docker run -d -p 8054:8050 --memory=3G --restart=always scrapinghub/splash:master --maxrss 2048 --disable-browser-caches 
```


```
http {
    upstream splash {
        least_conn;
        server localhost:8051;
        server localhost:8052;
        server localhost:8053;
        server localhost:8054;
    }
    server {
        listen 8050;
        location / {
            proxy_pass http://splash;
        }
    }
}

```


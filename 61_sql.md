```
取首行的做法
ROW_NUMBER() over (partition by live_id,goods_id order by alive_time desc) as rank
```

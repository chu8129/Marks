### 取首行的做法
```
ROW_NUMBER() over (partition by live_id,goods_id order by alive_time desc) as rank
```
### 加速insert/load
```
set GLOBAL innodb_flush_log_at_trx_commit = 0;
set global net_buffer_length=1000000;
set global max_allowed_packet=1000000000;
SET foreign_key_checks = 0;
SET UNIQUE_CHECKS=0;
SET GLOBAL general_log = 'OFF';
SET @@session.unique_checks = 0;
SET @@session.foreign_key_checks = 0;
SET AUTOCOMMIT = 0;
```

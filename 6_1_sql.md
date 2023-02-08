### 取首行的做法
```
ROW_NUMBER() over (partition by live_id,goods_id order by alive_time desc) as rank
```
### 加速insert/load
```
set GLOBAL innodb_flush_log_at_trx_commit = 0;
set global innodb_buffer_pool_size=10 * 1024 * 1024 * 1024;
set global innodb_log_buffer_size=1 * 1024 * 1024 * 1024;
set global net_buffer_length=1 * 1024 * 1024 * 1024;
set global max_allowed_packet=10 * 1024 * 1024 * 1024;
set global innodb_write_io_threads=8;
SET foreign_key_checks = 0;
SET UNIQUE_CHECKS=0;
SET GLOBAL general_log = 'OFF';
SET @@session.unique_checks = 0;
SET @@session.foreign_key_checks = 0;
SET AUTOCOMMIT = 0;
```
```
LOCK TABLES `tablename` WRITE;
ALTER TABLE  `tablename` DISABLE  KEYS ;
INSERT INTO `` VALUES (1,11,'UPDATED');
INSERT INTO `` VALUES (2,11,'UPDATED');
ALTER TABLE `` ENABLE KEYS;
UNLOCK TABLES;
```

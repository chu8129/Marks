### 启动
```
并行500一般建议，collect注意大小，需要的是driver
stanalone模式记得maxResultSize
还是amazon的emr省心，还是ssd硬盘，速度快很多，用完关闭省去了删除数据的步骤，比较建议spark配置不做删除，crontab起一个，原因：数据量大会超时导致报错

/data/spark-3.0.0-bin-hadoop3.2/bin/spark-submit 
--num-executors 2   
--executor-memory 8G 
--driver-memory 16G 
--executor-cores 1  
--conf spark.default.parallelism=1000 
--conf spark.driver.maxResultSize=8G 
--py-files code1105.zip 
***.py
```

### spark-env.sh
```
JAVA_OPTS="-Xms128m -Xmx1303m -Xss256k"
SPARK_LOCAL_DIRS=/中间数据路径/
#export SPARK_SSH_OPTS="-p 36000"
SPARK_WORKER_OPTS="-Dspark.worker.cleanup.enabled=false –Dspark.workder.cleanup.interval=1200"
export PYSPARK_DRIVER_PYTHON=/opt/virtualenv/mh_dm_spark/bin/python
export PYSPARK_PYTHON=/opt/virtualenv/mh_dm_sparkt/bin/python
```

### ValueError: Cannot run multiple SparkContexts at once; existing SparkContext(app=*.py, master=local[*])
```
```
sc = SparkContent.getOrCreate()
```

### map(lambda l:(l[0], l[1]))
```
map使用的lambda只能取一个否则报错
```

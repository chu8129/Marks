### 启动
```
并行500一般建议，collect注意大小，需要的是driver

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

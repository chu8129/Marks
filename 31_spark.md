### 个人喜好
```
真觉得rdd方便理解，也不用太多api
```
### 改spark原因
```
1、框架内代码风格还能骚出境界的，没几个人
2、api统一，逻辑统一，输出统一，强行保证统一
```
### spark-env.sh
```
JAVA_OPTS="-Xms128m -Xmx1303m -Xss256k"
SPARK_LOCAL_DIRS=/dirs/
#export SPARK_SSH_OPTS="-p 36000"
SPARK_WORKER_OPTS="-Dspark.worker.cleanup.enabled=false –Dspark.workder.cleanup.interval=12000"
export PYSPARK_DRIVER_PYTHON=/*env/bin/python
export PYSPARK_PYTHON=/*env/bin/python
```
### 启动
```
并行500一般建议，collect注意大小，需要的是driver
stanalone模式记得maxResultSize
还是amazon的emr省心，还是ssd硬盘，速度快很多，用完关闭省去了删除数据的步骤，
建议
  spark配置不做删除，crontab起一个
原因
  数据量大会超时导致报错
曾经听分享的时候
  美团：起个集群，几百台机器
  内心：我还在用着最小集群。。。

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


### ValueError: Cannot run multiple SparkContexts at once; existing SparkContext(app=*.py, master=local[*])
```
sc = SparkContent.getOrCreate()
```

### map(lambda l:(l[0], l[1]))
```
map使用的lambda只能取一个否则报错
```

### lazy
```
如果是用mysql准备好数据为文件再用spark读取，建议拆分为两个脚本，lazy操作会直接跳过了cache，然后启动spark的时候读取不存在
```

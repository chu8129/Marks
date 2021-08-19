### 问题复现
```
qw@wangqiuwens-Mac-mini Downloads % python3  test.py
('美妆个护|护肤|||', 10902)
('美妆个护|美妆|||', 10901)
qw@wangqiuwens-Mac-mini Downloads % python3  test.py
('美妆个护|美妆|||', 10901)
('美妆个护|护肤|||', 10902)
qw@wangqiuwens-Mac-mini Downloads % python3  test.py
('美妆个护|护肤|||', 10902)
('美妆个护|美妆|||', 10901)
qw@wangqiuwens-Mac-mini Downloads % python3  test.py
('美妆个护|美妆|||', 10901)
('美妆个护|护肤|||', 10902)
```
### 源码
```
qw@wangqiuwens-Mac-mini Downloads % cat test.py 
s = {('美妆个护|美妆|||', 10901), ('美妆个护|护肤|||', 10902)}
print(list(s))
```
### 猜测原因
set利用hash保证唯一，那么必须有个hash函数，由此有个基础的seed
seed的设置以及相关代码？
java的set顺序为何是一致的？
python的hash函数有哪些

### 疑问1:set的random-seed
```
cpython-source:keyword:PyTypeObject
```

### 疑问2:random-seed设置
```
export PYTHONHASHSEED=0
relevant site:https://hg.python.org/cpython/rev/6b7704fe1be1#l9.26
```

### 疑问3:java-random-seed问题
### 疑问4:py使用的hash函数

### 待续

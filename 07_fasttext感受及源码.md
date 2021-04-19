### 原因：满足了我日常所需且速度极为可观

## 个人感受
```
熟读Bag of Tricks for Efficient Text Classification(link:https://arxiv.org/abs/1607.01759)
```

```
关于类不平衡问题
建议：人为干预，虽然官方文档说处理比较完善，且外界评论极好
但:实际工程中，不平衡类别差距过大的时候，会偏向于某一类，特别是特征少的时候
可能的问题原因：min_count设置问题，或者你数据集本身有问题，也有可能是关键词提取
```

```
RuntimeError: Encountered NaN
建议是检查下自己的文本文件，预估是label处理问题，本人遇到的是量级不对(吧第一个词当作label了,原先想法是末尾)
```


## 记录

### 重点关注的点：202001
```
1、各loss function 计算方式
2、词hash表的构建确认
3、模型架构确认
```

```

202010：当前版本，fasttext0.9.1，其实ft最新是092，无奈setup写死了
202010：模型：hanlp.pretrained.pos.CTB5_POS_RNN_FASTTEXT_ZH:build_model
  layer tf.keras.utils.deserialize_keras_object(embeddings,custom_objects=tf.keras.utils.get_custom_objects())
  drop_out
  blstm
  drop_out
202010：
  如果使用Word2VecEmbedding/StringWord2VecEmbedding，则是concat模式
202010
  hanlp的词性很喜欢embedding，不过ctb6-pos-rnn < 100M，fasttext就是原始的3G了
202010
  百度词性，英文容易被分成xc，hanl(rnn有问题/fasttext较少)词性容易被分成pu，pu为不可接受，注释(其他虚词、标点)
  不知为何，词性往ner走的baidu-lac，对“喜茶“的结果很有问题
  hanlp会把空字符分为NN，诡异之处，猜测是训练集问题
  
202010
    2、[baidu更好]baidu-lac结果其实已经包含了NER结果，例如PER、LOC等，但热词模块无影响，都当作名词使用
    3、[baidu有问题]关于英文，baidu-lac结果，如kindom rush garrix等均被定义为xc(其他虚词)，hanlp目前结果有NR/NN
        baidu-lac对品牌词lancom/estee laude或名人Beyond正常
    4、[baidu/hanlp都有问题]baidu-lac会将空白字符串识别为n/w，大概率为w，hanlp识别为NN/CD，测试样例比例中基本差不多
    5、[baidu有问题]baidu-lac包含数字的均为m(量词)，如29岁/1/2/#3CE/三件套/2018款/四度 ，hanlp则会有NN/CD/NR等词性出来
    6、[hanlp有问题]hanlp部分动词判断错误，如修护NN/防晒霜NN，baidu-lac结果：修护v/防晒霜n
  
```

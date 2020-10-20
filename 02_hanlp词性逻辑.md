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
  hanlp优势会把空字符分为NN，诡异之处，猜测是训练集问题
  
  
```

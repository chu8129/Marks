```
原因：由于hanlpv2-large-albert的效率，想看看有没有优化手段；目前看来只能优化加载以及预测的过程，但过程逻辑比较精简，希望不大

关于分词：目前发现，几大分词，比较倾向hanlp
重点看了分词的tokenizer，
  使用的是公开的https://storage.googleapis.com/albert_models/albert_base_zh.tar.gz
  fit自己的预料，data/cws/large/all.txt
  参数耐心找会发现的～
```

```
代码中，各个模型的地址ALL，是运行时加载的，关键字:exec
```

```
加载large-albert流程
save_dir https://file.hankcs.com/hanlp/cws/large_cws_albert_base_20200828_011451.zip
metapath /Users/qw/.hanlp/cws/large_cws_albert_base_20200828_011451/meta.json
meta {'class_path': 'hanlp.components.tok.TransformerTokenizer', 'hanlp_version': '2.0.0-alpha.50'}
cls hanlp.components.tok.TransformerTokenizer
load config.json
>>>
```

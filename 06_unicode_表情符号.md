###
```
替换表情有两种方式
最直接的，替换表情和符号
 问题：表情需要整理，符号同理，但是unicode已经是unicode13了，范围能让你怀疑人生
反向，取中文数字英文
 问题：需要额外补充字符，例如日期2020/01/02 2021.01.01对分词算法还是有影响的，需要先保留后期剔除
两种都各有优劣，自行斟酌
```


### 偷懒方法
```
re.compile("[^\u4E00-\u9FA5A-Za-z0-9]")
```

### 表情
```
 34         self.re_sub = re.compile("[^\u4E00-\u9FA5A-Za-z0-9]")
 35         # https://www.codetable.net/decimal/8226
 36         # http://www.unicode.org/charts/
 37         numbers = set(str(n) for n in range(10))
 38         self.re_sub = re.compile(
 39             "("
 40             + "|".join(
 41                 [   
 42                     re.escape(u)
 43                     for language_list in emoji.core.unicode_codes.EMOJI_UNICODE.values()
 44                     for u in language_list
 45                     if u not in numbers
 46                 ] 
 47                 + [ 
 48                     re.escape(u)
 49                     for u in "\x14\x13\x12\x11".encode().decode("utf8")
 50                     + chr(8226)
 51                     + chr(10049)
 52                     + chr(9060)
 53                     + chr(9061)
 54                     + "⍢⃝'
 55                     + "๑˃̵ᴗ˂̵و"
 56                 ]
 57             ) 
 58             + ")"
 59         )
 ```
 ### 一些字符串
 ```
 60         re_string = (
 61             "["
 62             + "".join(
 63                 re.escape(u)
 64                 for u in """'＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､\u3000、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘    ’‛“”„‟…‧﹏﹑﹔·！？｡。!"#$%&'()*+,-./:;<=>-?@[]^_`{|}~ô’Åéãíç()!`\\"""
 65             ) 
 66             + "]"
 67         )
 68         logging.debug("re_string:%s", re_string)
 69         self.word_re_sub = re.compile(re_string)
 70     


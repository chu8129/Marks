```
[\u1f300-\u1f5ff\u1f900-\u1f9ff\u1f600-\u1f64f\u1f680-\u1f6ff\u2600-\u26ff\u2700-\u27bf\u1f1e6-\u1f1ff\u1f191-\u1f251\u1f004\u1f0cf\u1f170-\u1f171\u1f    17e-\u1f17f\u1f18e\u3030\u2b50\u2b55\u2934-\u2935\u2b05-\u2b07\u2b1b-\u2b1c\u3297\u3299\u303d\u00a9\u00ae\u2122\u23f3\u24c2\u23e9-\u23ef\u25b6\u23f8-\u23fa\U000100    00-\U0010ffff]
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


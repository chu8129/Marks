```
228     from functools import partial
229     from tqdm import tqdm as std_tqdm
231     tqdm = partial(std_tqdm, ncols=80)
```

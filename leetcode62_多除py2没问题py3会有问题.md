```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import reduce
        if m==0:
            return n
        if n == 0:
            return m
        m, n = max(m,n), min([m,n])
        m = m + n - 2
        n = n - 1
        la,lo,lo2 = map(lambda l:reduce(lambda a,b:a*b, l), [
        range(1,m+1) if m > 1 else [1,1],
        range(1,n+1) if n > 1 else [1,1],
        range(1,m-n+1) if m-n > 1 else [1,1],
        ])
        return int(la/(lo*lo2))
        # 注意，多次除法会有问题
```

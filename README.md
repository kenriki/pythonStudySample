# Python Study Sample Code

## study1 

```python
import webbrowser
import pathlib
import openpyxl
import os
```
> test.py でHTMLに書き込んで、ブラウザで自動展開で表示まで

## study2

> bubblesort.py でバブルソート（ランダム値を用いる) 実行
```python
def bubble_sort(data, n):
    for i in range(n):                                      # i=0からnまでのループ
        for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
            if data[j-1] > data[j]:                         # 隣り合う値を比較
                data[j], data[j-1] = data[j-1], data[j]     # 交換
    return data
```

> bubblesort_plot.py でバブルソートをプロットした際の動作を画像として出力できる
```python
import numpy as np
from matplotlib import pyplot as plt
```

## study3
> stackSample.py でスタックのアルゴリズムを理解

## study4
> sample1.py コンストラクタについて学ぶ  
> sample2.py ディープラーニングで画像認識する
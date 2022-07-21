import numpy as np
import pandas as pd




a = pd.Series({'0': 12, '1': 888, '2': '1wwww'}, name='jjjjjjj')
# a = pd.Series([1,2,3,4,5,6])
print(a)
s = pd.DataFrame(a)
print(s)

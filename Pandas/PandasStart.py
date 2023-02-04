import numpy as np

import pandas as pd

s= pd.Series([1,2,5,np.nan,6,8])
m = pd.Series(2,index=list(range(5)))
df = pd.DataFrame({"A":1.,
"b": pd.Timestamp('20130102'),
"c":pd.Series(1,index=list(range(10)),dtype="float32")})

print(s)
print(m)
print(df)
print(df.head())
print(df.tail())
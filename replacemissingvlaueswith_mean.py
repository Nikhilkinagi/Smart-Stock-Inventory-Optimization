import pandas as pd
import numpy as np
df = pd.read_csv("/Users/nikhil.kinagi/Downloads/smart-stock(1).csv")
df.fillna(method='ffill',inplace=True)
print(df.head(20)) 



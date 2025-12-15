import pandas as pd
import numpy as np
 
df = pd.read_csv("/Users/nikhil.kinagi/Downloads/smart-stock(1).csv")

print("Mean:\n",df['sales'].mean())

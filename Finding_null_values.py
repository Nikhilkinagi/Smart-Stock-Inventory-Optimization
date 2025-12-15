import pandas as pd
import numpy as np
def check_null_values(df):
    if df.isnull().any().any():
        print("Null values found.")
        print(df.isnull().sum())
    else:
        print("No null values found.")
df = pd.read_csv("/Users/nikhil.kinagi/Downloads/smart-stock(1).csv")
print(df)

check_null_values(df)

import pandas as pd

df = pd.read_csv("/Users/nikhil.kinagi/Downloads/smart-stock(1).csv")
df = df.drop("Product Name",axis=1)
print(df)
sorted_df = df.sort_values(by= df.columns[2])

print(sorted_df)

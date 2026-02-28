import sys
import pandas as pd 

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"name":["kunashe","elijah","gracious"], "age":[3,39,27]})
df["month"] = month
df.to_parquet(f"month={month}.parquet")
print(df.head())

print(f"Running pipeline for month {month}")

import pandas as pd

data = {
    "Name": ["Charles", "Leclerc", "Lewis", "Max", None],
    "Age": [24, 40, None, 35, 12],
    "salary": [43500, 57680, 68660, 57533, None],
}

df = pd.DataFrame(data)

df = df.drop_duplicates()
df = df.dropna()
df.columns = df.columns.str.lower()

print("first rows:\n", df.head())
print("\nInfo:\n")
df.info()
print("\nSummary:\n", df.describe())
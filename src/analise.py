import pandas as pd

df = pd.read_csv("data/vendas.csv")
df["data"] = pd.to_datetime(df["data"])

print("Primeiras linhas do dataset: ")
print(df.head())

print("\nInformações gerais: ")
df.info()

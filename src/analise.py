import pandas as pd

df = pd.read_csv("data/vendas.csv")

print("Primeiras linhas do dataset: ")
print(df.head())

print("\nInformações gerais: ")
print(df.info())

import pandas as pd

df = pd.read_csv("credit_risk_dataset.csv")

print(df.head())

print(df.shape)

df.info()

print(df.describe())

print(df.isnull().sum())

print(df['loan_status'].value_counts())
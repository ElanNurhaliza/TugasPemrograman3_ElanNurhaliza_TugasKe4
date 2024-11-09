import pandas as pd


data = {
    'A': [15, 25, 14],
    'B': [3, 12, 7]
}

df = pd.DataFrame(data)


df['Tambah'] = df['A'] + df['B']
df['Kurang'] = df['A'] - df['B']
df['Kali'] = df['A'] * df['B']
df['Bagi'] = df['A'] / df['B']


print(df)

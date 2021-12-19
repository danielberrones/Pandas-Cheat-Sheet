import pandas as pd

pd.set_option('max_rows',None)
df = pd.read_csv('bankData.csv',sep=';')

print(df)

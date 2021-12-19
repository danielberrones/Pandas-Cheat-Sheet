import pandas as pd

pd.set_option('max_rows',None)
df = pd.read_csv('/data/bankData.csv',sep=';')

print(df)

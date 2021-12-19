import pandas as pd

pd.set_option('max_rows',None)
df = pd.read_csv('./data/bankData.csv',sep=';')

print('df.describe()')
print(df.describe())

#                age        balance           day      duration      campaign         pdays      previous
#count  45211.000000   45211.000000  45211.000000  45211.000000  45211.000000  45211.000000  45211.000000
#mean      40.936210    1362.272058     15.806419    258.163080      2.763841     40.197828      0.580323
#std       10.618762    3044.765829      8.322476    257.527812      3.098021    100.128746      2.303441
#min       18.000000   -8019.000000      1.000000      0.000000      1.000000     -1.000000      0.000000
#25%       33.000000      72.000000      8.000000    103.000000      1.000000     -1.000000      0.000000
#50%       39.000000     448.000000     16.000000    180.000000      2.000000     -1.000000      0.000000
#75%       48.000000    1428.000000     21.000000    319.000000      3.000000     -1.000000      0.000000
#max       95.000000  102127.000000     31.000000   4918.000000     63.000000    871.000000    275.000000

print('df.columns')
print(df.columns)
#Index(['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
       #'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
       #'previous', 'poutcome', 'y'],
      #dtype='object')

print("df['job'].value_counts()")
print(df['job'].value_counts())
#blue-collar      9732
#management       9458
#technician       7597
#admin.           5171
#services         4154
#retired          2264
#self-employed    1579
#entrepreneur     1487
#unemployed       1303
#housemaid        1240
#student           938
#unknown           288
#Name: job, dtype: int64

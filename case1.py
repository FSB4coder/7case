#Case 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')

df.fillna(-1, inplace=True)

x = df[df['math score' <= '60']]
x = x[x['math score'] >= 90].values_count()
print(f'В {x} случаях да, в {len(df.index) - x} нет')

s = pd.Series(data=df['parental level of education'], index=df['math score'])
s.plot()
plt.show()

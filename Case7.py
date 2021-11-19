#Case 7
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('investments_VC.csv')

df.fillna(-1, inplace=True)

x = df['first_funding_at']
z = df['last_funding_at']
print(f'Первое финансирование будет больше на {x - z} чем последнее')

s = pd.Series(data=x, index=z)
s.plot()
plt.show()

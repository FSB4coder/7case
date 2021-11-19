#Case 3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

df.fillna(-1, inplace=True)

x = df['Cholesterol']
z = df['Cholesterol (% Daily Value)']

print(f'Если число ушло в минус, то у вас избыток хлорестерина. Если в плюсе, то у вас недостаток хлорестерина. {z-x}')
s = pd.Series(data=x, index=z)
s.plot()
plt.show()

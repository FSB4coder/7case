#Case2
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('countries of the world.csv')

df.fillna(-1, inplace=True)

x = df['Literacy (%)']
z = df['Phones (per 1000)']
x1 = x.values_counts()
z1 = z.values_counts()
print(f'Телефоны влияют на грамотность человека примерно на {x1 - z1} %')
s = x
s.plot(kind='hist')
s1 = z
s1.plot(kind='hist')
plt.show()

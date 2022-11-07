import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/liza/Desktop/LAB2/DS5.txt', sep=' ',header=None)

plt.figure(figsize=(9.6,5.4))
plt.scatter(df[1], df[0])
plt.show()
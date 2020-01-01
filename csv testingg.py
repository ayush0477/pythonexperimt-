import pandas as pd
import numpy as np
import matplotlib as plt
f = pd.read_csv('file://localhost/C:/Users/AYush/Downloads/Airplane_Crashes_and_Fatalities_Since_1908.csv')
print(f)
d = f.loc[:,"Date"]
u = f.loc[:,"Summary"]
t = f. loc[:,"Time"]
N = 50

colors = np.random.rand(N)
area = (30 * np.random.rand(d))**2
area = (30 * np.random.rand(t))**2
plt.scatter(d, t, s=area, c=colors, alpha=0.5)
plt.show()
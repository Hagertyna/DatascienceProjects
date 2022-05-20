import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('fivethirtyeight')

mu = 80
sigma = 7
x = np.random.normal(mu, sigma, size=200)

fig, ax = plt.subplots()

ax.hist(x, 20)
ax.set_title("New Historgram")
ax.set_xlabel('bin range')
ax.set_ylabel('frequency')

fig.tight_layout()
plt.show()

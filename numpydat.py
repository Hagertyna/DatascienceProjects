# 1. Imports
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
%matplotlib inline

# 2. Define data
x = np.arange(0, 4 * np.pi, 0.2)
y = np.sin(x)


# 3. Plot data including options
plt.plot(x, y,
    linewidth=0.5,
    linestyle='--',
    color='r',
    marker='o',
    markersize=10,
    markerfacecolor=(1, 0, 0, 0.1))


# 4. Add plot details
plt.title('Plot of sin(x) vs x from 0 to 4 pi')
plt.xlabel('x (0 to 4 pi)')
plt.ylabel('sin(x)')
plt.legend(['sin(x)']) # list containing one string
plt.xticks(
    np.arange(0, 4*np.pi + np.pi/2, np.pi/2),
    ['0','pi/2','pi','3pi/2','2pi','5pi/2','3pi','7pi/2','4pi'])
plt.grid(True)


# 5. Show the plot
plt.show()

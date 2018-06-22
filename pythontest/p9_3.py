import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(1000)


matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(100*np.random.randn(100), 100*np.random.randn(100), '*')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()

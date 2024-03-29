from matplotlib import pyplot as plt
import numpy as np

x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()

ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

x=np.arange(1,11)
y=2*x

plt.title("Line plot")
plt.xlabel("x Axis")
plt.ylabel("y Axis")

plt.plot(x,y)
plt.show()
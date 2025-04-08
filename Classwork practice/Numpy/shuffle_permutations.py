from numpy import random
import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,10])
random.shuffle(x)
print("\n",x)


print("\n",random.permutation(x))
import numpy as np
import pickle
import matplotlib.pyplot as plt


#grid = np.random.random((10, 10))
#print grid
#
#fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, figsize = (6,10))
#
#ax1.imshow(grid, extent = [0, 100, 0 ,1])
#ax1.set_title("Default")
#
#ax2.imshow(grid, extent = [0, 100, 0 ,1], aspect = "auto")
#ax2.set_title("Auto-scaled Aspect")
#
#ax3.imshow(grid, extent=[0, 100, 0, 1], aspect = 100)
#ax3.set_title("Manually Set Aspect")

#plt.tight_layout()
#plt.show()

with open("deneme.dat", "rb") as fi:
	obj = pickle.load(fi)

obj2 = obj[:100,:1000]
print len(obj2), len(obj2[0])
plt.imshow(obj2, extent = [0, len(obj2[0]), 0, len(obj2)], aspect = "auto")
plt.tight_layout
plt.show()

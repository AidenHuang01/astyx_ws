import numpy as np
import matplotlib.pyplot as plt

seg = np.load("seg.npy")
bev = np.load("bev.npy")
segs_bev = np.load("segs_bev.npy")

seg = np.argmax(seg, axis=1)
seg = np.squeeze(seg)

seg[seg!=2] = 8
#bev[bev==0] = 255
plt.imshow(seg[:,:])#, cmap=plt.get_cmap("YlGnBu"))
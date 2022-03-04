from dis import dis
import astyx_utils
from astyx_utils import *
import matplotlib.pyplot as plt
import pdb

data = Astyx_Data()
img = data.get_camera("000100")

params = data.get_calibration_details()

proj = astyx_projection(params)

lidar_pc = data.get_lidar("000100")
print(lidar_pc.shape)
lidar_image = proj.lidar2CameraAstyx(lidar_pc[:,:3])
dist = np.linalg.norm(lidar_pc[:,:3],axis=1)
print("dist.max(): ", dist.max())
lidar_image = lidar_image.astype(int)
print(lidar_image.shape)
print("img.shape: ", img.shape)
print("lidar_image.shape: ", lidar_image.shape)

print("max dim 1: ", lidar_image[:,1].max())
print("max dim 0: ", lidar_image[:,0].max())

####
print("========================experiment space========================")
print("lidar_pc.shape: ", lidar_pc.shape)
lidar_xyz = lidar_pc[:3]

print("========================experiment space========================")
####


radius = 6

for i in range(lidar_image.shape[0]):
    if lidar_image[i,1] < img.shape[0]-radius and lidar_image[i,0] < img.shape[1]-radius and lidar_image[i,1] >= radius and lidar_image[i,0] >= radius:
        img[lidar_image[i,1]-radius : lidar_image[i,1]+radius+1,
        lidar_image[i,0]-radius : lidar_image[i,0]+radius+1,
        :] = 255
print(dist.shape)
# empty[lidar_image[0,1],lidar_image[0,0],:] = 255
# pdb.set_trace()
# lidar_img = np.zeros()

plt.imshow(img)
plt.show()
import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_voxels(array_3d: np.array):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('auto')
    ax.voxels(array_3d, edgecolor="k")
    plt.show()

# make quadraped by removing voxels from a cube
grid_size = 10
target = np.zeros(shape = (grid_size,grid_size,grid_size),dtype = int)
body_span = 5
target[:body_span, :body_span, :body_span+2] = 1
target[1:body_span-1, :, :body_span - 1] = 0
target[:,1:body_span-1, :body_span - 1] = 0
plot_voxels(target)
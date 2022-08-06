from email.quoprimime import body_length
import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

def plot_voxels(array_3d: np.array):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('auto')
    ax.voxels(array_3d, edgecolor="k")
    plt.show()

# make quadraped by removing voxels from a cube
def simple_quadraped():
    grid_size = 10
    target = np.zeros(shape = (grid_size,grid_size,grid_size),dtype = int)
    body_span = 5
    target[:body_span, :body_span, :body_span+2] = 1
    target[1:body_span-1, :, :body_span - 1] = 0
    target[:,1:body_span-1, :body_span - 1] = 0
    return target

def quadraped_from_paper():
    # I Shape
    grid_size = 10
    target = np.zeros(shape = (grid_size,grid_size,grid_size),dtype = int)
    body_span = 8
    body_length = 8
    height = 5
    target[0, grid_size//2 - int(0.5*body_span): grid_size//2 + int(0.5*body_span), height] = 1
    target[body_length, grid_size//2 - int(0.5*body_span): grid_size//2 + int(0.5*body_span), height] = 1
    target[0:body_length, grid_size//2, height] = 1
    return target
    
target = quadraped_from_paper()
plot_voxels(target)
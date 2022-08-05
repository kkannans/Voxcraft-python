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

@dataclass
class vector:
    x:float
    y:float
    z:float

grid_size = 10
target = np.zeros(shape=(grid_size,grid_size,grid_size), dtype = int)
torso_dim = vector(3.0, 2.0, 1.0)
leg_dim = vector(1.0, 1.0, 2.0)
torso_origin = vector(grid_size//2, grid_size//2, torso_dim.z + leg_dim.z)

def make_torso(target:np.array, torso_origin:vector, torso_dim:vector):
    start_x = int(torso_origin.x - torso_dim.x/2.0)
    end_x = int(torso_origin.x + torso_dim.x/2.0)
    start_y = int(torso_origin.y - torso_dim.y/2.0)
    end_y = int(torso_origin.y + torso_dim.y/2.0)
    start_z = int(torso_origin.z - torso_dim.z/2.0)
    end_z = int(torso_origin.z + torso_dim.z/2.0)
    print(start_x ,end_x)
    print(start_y ,end_y)
    print(start_z ,end_z)
    target[start_x : end_x, start_y : end_y, start_z : end_z] = 1
    return target

def add_legs(target:np.array, leg_dim:vector):
    # get 4 corner indices of the torso
    min_coordinate = np.min(target == 1)
    max_coordinate = np.max(target == 1)
    print(min_coordinate, max_coordinate)
    front_left = vector() 
    return target


target = make_torso(target, torso_origin, torso_dim)
plot_voxels(target)
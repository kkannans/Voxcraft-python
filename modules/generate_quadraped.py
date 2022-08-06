from email.quoprimime import body_length
from inspect import BoundArguments
from multiprocessing.dummy import active_children
from statistics import mean
import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import math

def plot_voxels(array_3d: np.array):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_aspect('auto')
    ax.voxels(array_3d, facecolors="blue", edgecolor="k")
    plt.show()


class Body_Generator:
    def __init__(self) -> None:
       self.target = None

    def I_template(self, grid_size = 10):
        self.target = np.zeros(shape = (grid_size,grid_size,grid_size),dtype = int)
        # I Shape
        body_span = 8
        body_length = 8
        height = 5
        self.target[0,grid_size//2 - int(0.5*body_span):grid_size//2 + int(0.5*body_span), height] = 1
        self.target[body_length,grid_size//2 - int(0.5*body_span):grid_size//2 + int(0.5*body_span), height] = 1
        self.target[0:body_length,grid_size//2, height] = 1
        return self.target
    
    def generate_simple_quadraped(self, grid_size = 10):
        self.target = np.zeros(shape = (grid_size,grid_size,grid_size),dtype = int)
        body_span = 5
        self.target[:body_span, :body_span, :body_span+2] = 1
        self.target[1:body_span-1, :, :body_span - 1] = 0
        self.target[:,1:body_span-1, :body_span - 1] = 0
        return self.target

    def get_body_coordinates(self):
        return np.where(self.target == 1)

    def get_actuators_from_paper(self, actuator_material_value = 2):
        body_coordinates = self.get_body_coordinates()
        self.target[min(body_coordinates[0]), mean(body_coordinates[1]), min(body_coordinates[2])] = actuator_material_value
        self.target[max(body_coordinates[0]), mean(body_coordinates[1]), min(body_coordinates[2])] = actuator_material_value

if __name__ =="__main__":
    bg = Body_Generator()
    bg.I_template()
    bg.get_actuators_from_paper()
    plot_voxels(bg.target)
    print(np.unique(bg.target))
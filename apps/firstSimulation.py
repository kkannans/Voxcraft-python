import numpy as np
import os
from modules.VoxcraftVXA import VXA
from modules.VoxcraftVXD import VXD
from modules.generate_quadraped import *

data_path = os.getcwd() + "/data"
if not os.path.exists(data_path):
    os.makedirs(data_path)
# Generate a Base VXA file
# See here for list of vxa tags: https://gpuvoxels.readthedocs.io/en/docs/
vxa = VXA(EnableExpansion=1, SimTime=5) # pass vxa tags in here

# Create two materials with different properties
mat1 = vxa.add_material(RGBA=(255,0,255), E=5e4, RHO=1e4) # returns the material ID
mat2 = vxa.add_material(RGBA=(255,0,0), E=1e8, RHO=1e4)


# Write out the vxa to data/ directory
base_vxa_path = data_path + "/base.vxa"
vxa.write(base_vxa_path)

I_shaped_body = quadraped_from_paper()
body = np.random.randint(0,mat2+1,size=(5,5,5))

# Generate a VXD file (to configure a single simulation)
vxd = VXD()
vxd.set_tags(RecordVoxel=1) # pass vxd tags in here to overwite vxa tags
vxd.set_data(body)
# Write out the vxd to data/
base_vxd_path = data_path+"/robot.vxd"
vxd.write(base_vxd_path)
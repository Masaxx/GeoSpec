import numpy as np
from PIL import Image

def generate_orthophoto(rgb_file, nir_file=None):
    # Mock orthophoto generation (in real use: Pix4D/ERDAS stitching)
    rgb = np.array(Image.open(rgb_file).convert("RGB"))
    if nir_file:
        nir = np.array(Image.open(nir_file).convert("L"))
        # Stack to 4-channel
        ortho = np.dstack((rgb, nir))
    else:
        ortho = rgb
    return ortho  # returns numpy array ready for model
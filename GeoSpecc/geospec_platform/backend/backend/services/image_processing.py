import cv2
import numpy as np

def preprocess_multispectral(image):  # image: (H,W,4) or separate bands
    if len(image.shape) == 3 and image.shape[2] == 4:
        image = image / 255.0
        return cv2.resize(image, (256, 256))
    return image / 255.0

def compute_ndvi(red, nir):
    red = red.astype(np.float32)
    nir = nir.astype(np.float32)
    ndvi = (nir - red) / (nir + red + 1e-8)
    return np.clip(ndvi, -1, 1)
import numpy as np
from skimage.exposure import equalize_adapthist
from dehaze.exposure_fusion import exposure_fusion

def amef(I_hazy, clip_range):
    I = np.zeros((*I_hazy.shape, 6))
    I[:, :, :, 0] = I_hazy

    for i in range(1, 5):
        gamma = i + 1
        I[:, :, :, i] = np.power(I_hazy, gamma)

    for c in range(3):
        I[:, :, c, 5] = equalize_adapthist(I_hazy[:, :, c], clip_limit=clip_range)

    R = exposure_fusion(I)
    return R

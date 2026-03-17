import numpy as np
import cv2
from dehaze.pyramid_operations import gaussian_pyramid, laplacian_pyramid, reconstruct_laplacian_pyramid

def exposure_fusion(I):
    r, c, _, N = I.shape
    W = np.ones((r, c, N)) * contrast(I) * saturation(I)

    W += 1e-12
    W /= np.sum(W, axis=2, keepdims=True)

    pyr = gaussian_pyramid(np.zeros((r, c, 3)))
    nlev = len(pyr)

    for i in range(N):
        pyrW = gaussian_pyramid(W[:, :, i])
        pyrI = laplacian_pyramid(I[:, :, :, i])

        for l in range(nlev):
            w = np.repeat(pyrW[l][:, :, np.newaxis], 3, axis=2)
            pyr[l] += w * pyrI[l]

    R = reconstruct_laplacian_pyramid(pyr)
    return R

def contrast(I):
    h = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    C = np.zeros((I.shape[0], I.shape[1], I.shape[3]))
    for i in range(I.shape[3]):
        mono = np.dot(I[:, :, :, i], [0.2989, 0.5870, 0.1140])
        C[:, :, i] = np.abs(cv2.filter2D(mono, -1, h))
    return C

def saturation(I):
    C = np.zeros((I.shape[0], I.shape[1], I.shape[3]))
    for i in range(I.shape[3]):
        R, G, B = I[:, :, 0, i], I[:, :, 1, i], I[:, :, 2, i]
        mu = (R + G + B) / 3
        C[:, :, i] = np.sqrt(((R - mu)**2 + (G - mu)**2 + (B - mu)**2) / 3)
    return C

import cv2
import numpy as np

def gaussian_pyramid(I, nlev=None):
    pyr = [I]
    filter = pyramid_filter()
    for _ in range(1, nlev or int(np.log2(min(I.shape[:2])))):
        I = downsample(I, filter)
        pyr.append(I)
    return pyr

def laplacian_pyramid(I, nlev=None):
    pyr = []
    filter = pyramid_filter()
    for _ in range(1, nlev or int(np.log2(min(I.shape[:2])))):
        next_level = downsample(I, filter)
        upsampled = upsample(next_level, filter, I.shape)
        pyr.append(I - upsampled)
        I = next_level
    pyr.append(I)
    return pyr

def reconstruct_laplacian_pyramid(pyr):
    filter = pyramid_filter()
    R = pyr[-1]
    for level in reversed(pyr[:-1]):
        R = level + upsample(R, filter, level.shape)
    return R

def pyramid_filter():
    return np.array([0.0625, 0.25, 0.375, 0.25, 0.0625])

def downsample(I, filter):
    return cv2.pyrDown(cv2.filter2D(I, -1, filter))

def upsample(I, filter, output_shape):
    up = cv2.pyrUp(I)
    up = cv2.filter2D(up, -1, filter)
    return up[:output_shape[0], :output_shape[1], :]

# Functions inspited by the Robert Bristow-Johnson (RBJ) cookbook
# http://www.musicdsp.org/files/Audio-EQ-Cookbook.txt

import numpy as np

def peak(peak_gain, Q):
    A = np.sqrt(peak_gain)
    def H(s):
        S2 = s**2
        return (S2 + s*(A/Q) + 1) / (S2 + s/(A*Q) + 1)
    return H

"""

tnl_util.py

Description: cd
Currently WIP.

Author: Jeremy Savarin

"""

import math
import numpy as np


def dat_tracker(filename, T, n_pts, n_ch):
    """
    Loads data from .dat, .lfp, or .fil files used in Neuroscope. Specify the
    center time, the duration, and the number of channels.

    Args:
        filename: name of file to load -> String
        T: center time (in samples) -> int64 or np.array(int64)
        n_pts: number of samples to load (centered at T) -> int64
        n_ch: number of channels in file -> int64

    Returns:
        data: 3D matrix of [channel number, data, T]
    """

    # Find number of points to shift
    if n_pts % 2:
        shift = n_pts/2
    else:
        shift = math.ceil(n_pts / 2)

    t_center = T - shift

    if t_center < 0:
        raise ValueError('Sample ranges passes beginning of data trace.')
    else:
        data = np.zeros((n_ch, n_pts, t_center.size))

        #  Read in data from file
        for i in range(0, t_center.size):
            with open(filename, 'r') as file:
                file.seek(2*n_ch*t_center[i])
                data[:, :, i] = np.fromfile(file, dtype=np.int16,
                                            count=n_ch*n_pts) \
                                  .reshape((n_ch, n_pts), order='F')

    return data

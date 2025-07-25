import os
import math
import numpy as np


def makedirs(path, mode=0o777, exist_ok=False):
    try:
        os.makedirs(path, mode=mode, exist_ok=exist_ok)
    except TypeError:
        if not os.path.exists(path):
            os.makedirs(path, mode=mode)


def isnan(x):
    return math.isnan(x)


def char2index(ch):
    if ch in ('A', 'a'):
        return 0
    elif ch in ('C', 'c'):
        return 1
    elif ch in ('G', 'g'):
        return 2
    elif ch in ('T', 't'):
        return 3
    elif ch in ('N', 'n'):
        return -1
    else:
        raise ValueError('Invalid base encountered.')


def one_hot_encode_sequence(seq, encoded):
    """
    Args:
        seq: str, DNA sequence
        encoded: numpy array of shape (len(seq), 4)
    """
    if encoded.shape[0] != len(seq):
        raise ValueError('encoded array not the same length as given seq')

    if encoded.shape[1] != 4:
        raise ValueError('encoded array needs to have 4 columns')

    for row_idx, base in enumerate(seq):
        col_idx = char2index(base)
        if col_idx >= 0:
            encoded[row_idx, col_idx] = 1.0
        else:
            encoded[row_idx, :] = 0.25


def nan_to_zero(arr):
    """
    Args:
        arr: 1D numpy array
    """
    arr[np.isnan(arr)] = 0.0


#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices"""

    return np.matmul(np.array(m_a), np.array(m_b))

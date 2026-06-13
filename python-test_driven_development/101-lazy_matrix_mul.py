#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    a = np.array(m_a)
    b = np.array(m_b)
    if a.ndim == 0 or b.ndim == 0:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    return np.matmul(a, b)

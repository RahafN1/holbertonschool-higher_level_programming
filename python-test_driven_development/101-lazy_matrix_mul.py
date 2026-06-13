#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    try:
        a = np.array(m_a)
        b = np.array(m_b)
    except ValueError:
        raise ValueError("setting an array element with a sequence.")

    if a.dtype == object or b.dtype == object:
        raise ValueError("setting an array element with a sequence.")

    if a.shape == () or b.shape == ():
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if a.ndim != 2 or b.ndim != 2 or a.shape[1] != b.shape[0]:
        return np.dot(a, b)
    return np.einsum('ij,jk->ik', a, b)

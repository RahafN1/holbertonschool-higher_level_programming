#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        numpy.ndarray: product of m_a and m_b
    """
    return np.dot(m_a, m_b)

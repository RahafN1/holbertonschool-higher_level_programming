#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""

    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        a = np.array(m_a)
        b = np.array(m_b)

        if len(a.shape) == 2 and len(b.shape) == 2:
            raise ValueError(
                "shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)"
                .format(
                    a.shape,
                    b.shape,
                    a.shape[1],
                    b.shape[0]
                )
            )

        raise

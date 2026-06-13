#!/usr/bin/python3
"""
Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a: first matrix (list of lists of int/float)
        m_b: second matrix (list of lists of int/float)

    Returns:
        New matrix that is the product of m_a and m_b

    Raises:
        TypeError: various validation errors
        ValueError: empty matrix or incompatible dimensions
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for n in row:
            if not isinstance(n, (int, float)) or isinstance(n, bool):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for n in row:
            if not isinstance(n, (int, float)) or isinstance(n, bool):
                raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_b)):
                value += m_a[i][k] * m_b[k][j]
            new_row.append(value)
        result.append(new_row)
    return result

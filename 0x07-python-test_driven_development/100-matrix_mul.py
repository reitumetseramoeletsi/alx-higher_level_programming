#!/usr/bin/python3
"""a module for a function that multiplies 2 matrices """


def matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices
    Args:
        m_a: the first matrice
        m_b: the second matrice
    Returns:
        matrice: a product of m_a * m_b
    Raises:
        TypeError: If m_a or m_b are not lists
        TypeError: If m_a or m_b are not lists of lists
        TypeError: If m_a or m_b Contain not int nor float
        TypeError: If m_a or m_b are not rectangular
        ValueError: If m_a or m_b are empty lists or matrice
        ValueError: If m_a or m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_notrect = False
    m_b_notrect = False
    m_a_notnum = False
    m_b_notnum = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnum = True
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrect = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")
    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")
    if m_a_notrect:
        raise TypeError("each row of m_a must be of the same size")
    if m_b_notrect:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = [[] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b)):
            k = 0
            for l in range(len(m_b)):
                k += m_a[i][l] * m_b[l][j]
            res[i].append(k)
    return res

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")

import math


def pascal_triangle(n):
    """
    Generates Pascal's triangle with n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
        Each inner list corresponds to a row in the triangle.
    """
    matrix = []

    for x in range(n):
        rows = []

        for y in range(x + 1):
            result = math.comb(x, y)
            rows.append(result)

        matrix.append(rows)

    return matrix

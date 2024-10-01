def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists, where each inner list represents a row
        in Pascal's triangle. If n <= 0, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row.

    for index in range(1, n):
        prev_row = triangle[-1]  # Get the last row added to the triangle.
        new_row = [1]  # Start the new row with 1.

        # Calculate the values for the new row based on the previous row.
        for index_2 in range(1, index):
            new_row.append(prev_row[index_2 - 1] + prev_row[index_2])

        new_row.append(1)  # End the new row with 1.
        triangle.append(new_row)  # Add the new row to the triangle.

    return triangle

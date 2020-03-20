def eigenvalue_2x2(matrix):
    import math

    result1 = (matrix[0][0] + matrix[1][1]) / 2 + math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    result2 = (matrix[0][0] + matrix[1][1]) / 2 - math.sqrt(
        ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

    return result1, result2


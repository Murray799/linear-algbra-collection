def VM_multiplication(vector, matrix):
    for element in range(len(vector)):
        try:
            for column in range(len(matrix[element])):
                matrix[element][column] = matrix[element][column]*vector[element]
        except IndexError:
            "incorrect dimensions please check input"

    for new in range(len(vector)):
        vector[new] = 0
        try:
            for col in range(len(matrix)):
                vector[new] += matrix[col][new]
        except IndexError:
            "incorrect dimensions please check input"

    return vector





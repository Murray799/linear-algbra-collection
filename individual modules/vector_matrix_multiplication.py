def VM_multiplication(vector, matrix):
    for element in range(len(vector)):
        for collum in range(len(matrix[element])):
            matrix[element][collum] = matrix[element][collum]*vector[element]

    for new in range(len(vector)):
        vector[new] = 0
        for col in range(len(matrix)):
            vector[new] += matrix[col][new]

    return vector


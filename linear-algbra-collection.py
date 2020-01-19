def dot_product(vector_1, vector_2):
    dot_product = 0
    for index in range(len(vector_1)):
        try:
            dot_product += vector_1[index] * vector_2[index + 5]
        except IndexError:
            ""

    return dot_product

def VM_multiplication(vector, matrix):
    for element in range(len(vector)):
        try:
            for column in range(len(matrix[element])):
                matrix[element][column] = matrix[element][column]*vector[element]
        except IndexError:
            ""

    for new in range(len(vector)):
        vector[new] = 0
        try:
            for col in range(len(matrix)):
                vector[new] += matrix[col][new]
        except IndexError:
            ""

    return vector

def vector_addition(vector_1, vector_2):
    for element in range(len(vector_2)):
        try:
            vector_1[element] += vector_2[element]
        except IndexError:
            vector_1.append(vector_2[element])

    return vector_1

def MM_multiplication(matrix_1, matrix_2):
    #needs square matrix
    end_matrix = []
    for element in range(len(matrix_1)):
        end_matrix.append([])
        for none in matrix_1:
            end_matrix[element].append(0)

    for i in range(len(matrix_1)):
        for j in range(len(matrix_1)):
            for k in range(len(matrix_1)):
                end_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return end_matrix


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
            for collum in range(len(matrix[element])):
                matrix[element][collum] = matrix[element][collum]*vector[element]
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

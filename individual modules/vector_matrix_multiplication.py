def VM_multiplication(vector, matrix):
    for element in range(len(vector)):
        # goes through the matrix and then multiplies with correct vector element
        try:
            for column in range(len(matrix[element])):
                matrix[element][column] = matrix[element][column]*vector[element]
        except IndexError:
            "incorrect dimensions please check input"

    for new in range(len(vector)):
        # empties vector 
        vector[new] = 0
        # adds matrix columns together and then adds to vector
        try:
            for col in range(len(matrix)):
                vector[new] += matrix[col][new]
        except IndexError:
            "incorrect dimensions please check input"

    return vector





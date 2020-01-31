def half_rotation(matrix):

    def MM_multiplication(matrix_1, matrix_2):
        end_matrix = []
        for element in range(len(matrix_1)):
            end_matrix.append([])
            for no_use in matrix_1:
                end_matrix[element].append(0)

        for i in range(len(matrix_1)):
            for j in range(len(matrix_1)):
                for k in range(len(matrix_1)):
                    end_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

        return end_matrix

    new_ = []
    for c in range(len(matrix)):
        new_.append([])
        for no_use in matrix:
            new_[c].append(0)
    count = 0
    for col in range(len(new_)):
        count += 1
        new_[col][count*-1] = 1

    return MM_multiplication(matrix, new_)


def MM_multiplication(matrix_1, matrix_2):
    count = 0
    for vector in matrix_1:
        for element in range(len(vector)):
            try:
                for collum in range(len(matrix_2[element])):
                    print("vector")
                    print(vector[element])
                    print("matrix")
                    print(matrix_2[element][collum])
                    matrix_2[element][collum] = matrix_2[element][collum] * vector[element]
            except IndexError:
                "hmm"


        print(matrix_2)

        for new in range(len(vector)):
            vector[new] = 0
            try:
                for col in range(len(matrix_2)):
                    vector[new] += matrix_2[col][new]
            except IndexError:
                "hmm"
        matrix_1[count] = vector
        count += 1

    return matrix_1

print(MM_multiplication([[3, 0],[0,3]],[[0,1],[1,0]]))

def MM_multiplication(vec):
    #needs square matrix
    from web_app_tool import final_step
    matrix_1, matrix_2 = final_step(vec)

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
print(MM_multiplication([[3,2],[1,4]],[[2,3],[4,1]]))

print(MM_multiplication([[14,11],[18,7]],[[0,1],[1,0]]))


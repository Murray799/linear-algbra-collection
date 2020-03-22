def eigen_vectore_2x2(matrix):
    def eigenvalue_2x2(matrix):
        import math

        result1 = (matrix[0][0] + matrix[1][1]) / 2 + math.sqrt(
            ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

        result2 = (matrix[0][0] + matrix[1][1]) / 2 - math.sqrt(
            ((matrix[0][0] + matrix[1][1]) / 2) ** 2 - matrix[0][0] * matrix[1][1])

        return result1, result2

    matrix[0,0] -= eigenvalue_2x2(matrix)
    matrix[1,1] -= eigenvalue_2x2(matrix)

    def solve_eq(matrix, result):
        def abs(lis):
            if lis < 0:
                lis = lis * -1
            return lis

        for k in range(len(result)):
            if abs(matrix[k][k]) < 0:
                for i in range(k + 1, len(result)):
                    if abs(matrix[i][k]) > abs(matrix[k][k]):
                        for j in range(k, len(result)):
                            matrix[k][j], matrix[i][j] = matrix[i][j], matrix[k][j]
                        result[k], result[i] = result[i], result[k]
                        break
            pivot = matrix[k][k]
            for j in range(k, len(result)):
                matrix[k][j] /= pivot
            result[k] /= pivot

            for i in range(len(result)):
                if i == k or matrix[i][k] == 0:
                    continue
                factore = matrix[i][k]
                for j in range(k, len(result)):
                    matrix[i][j] -= factore * matrix[k][j]
                result[i] -= factore * result[k]
        return matrix, result

    return solve_eq(matrix, [0,0])


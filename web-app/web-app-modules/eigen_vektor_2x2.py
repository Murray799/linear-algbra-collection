def eigen_vectore_2x2(matrix):
    from eigenvalue_for_2x2 import eigenvalue_2x2
    from web_app_tool import string_matrix
    from solve_eq import solve_eq
    matrix = string_matrix(matrix)

    matrix[0,0] -= eigenvalue_2x2(matrix)
    matrix[1,1] -= eigenvalue_2x2(matrix)


    return solve_eq(matrix, [0,0])


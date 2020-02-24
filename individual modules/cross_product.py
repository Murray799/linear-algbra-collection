def cross_product(vector_1, vector_2):
    new_vector = [1, 1, 1]

    new_vector[0] *= vector_1[1]*vector_2[2] - vector_1[2]*vector_2[1]
    new_vector[1] *= vector_1[2]*vector_2[0] - vector_1[0]*vector_2[2]
    new_vector[2] *= vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0]

    return new_vector

def dot_product(vector_1, vector_2):
    dot_product = 0
    for index in range(len(vector_1)):
        try:
            dot_product += vector_1[index] * vector_2[index + 5]
        except IndexError:
            ""

    return dot_product

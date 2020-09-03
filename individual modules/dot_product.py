def dot_product(vector_1, vector_2):
    dot_product = 0
    for index in range(len(vector_1)):
        try:
            dot_product += vector_1[index] * vector_2[index]
            # multiplies elements of the two vector and then adds it two dot_product
        except IndexError:
            "incorrect dimensions please check input"
            # checks for IndexError  

    return dot_product

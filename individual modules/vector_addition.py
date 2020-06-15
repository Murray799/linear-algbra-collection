def vector_addition(vector_1, vector_2):
    for element in range(len(vector_2)):
        # goes through all elements in Vector
        try:
            vector_1[element] += vector_2[element]
        except IndexError:
            vector_1.append(vector_2[element])

    return vector_1


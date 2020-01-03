
def dot_product(vector_1, vector_2):
    result = 0
    for index in range(len(vector_1)):
        try:
            result += vector_1[index] * vector_2[index + 5]
        except IndexError:
            ""

    return result

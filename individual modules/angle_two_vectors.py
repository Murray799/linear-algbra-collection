def angle(vector_1, vector_2):
    import math
    def dot_product(vector_1, vector_2):
        dot_product = 0
        for index in range(len(vector_1)):
            try:
                dot_product += vector_1[index] * vector_2[index]
            except IndexError:
                ""

        return dot_product

    def absolute_value(vector):
        import math
        val = 0

        for element in vector:
            val += element ** 2

        return math.sqrt(val)

    return math.acos(dot_product(vector_2,vector_1)/absolute_value(vector_2)*absolute_value(vector_1))

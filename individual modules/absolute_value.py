def absolute_value(vector):
    import math
    val = 0

    for element in vector:
        val += element**2

    return math.sqrt(val)


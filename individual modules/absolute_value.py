def absolute_value(vector):
    import math
    # impor the sqrt function from standart math module
    val = 0
    # defines variable

    for element in vector:
        val += element**2
        # adds the squares of all vectore elements to variable

    return math.sqrt(val)


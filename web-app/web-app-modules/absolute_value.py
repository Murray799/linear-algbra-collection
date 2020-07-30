def absolute_value(vector):
    from web_app_tool import string_vector
    vector = string_vector(vector)
    import math
    from web_app_tool import string_vector
    vector = string_vector(vector)

    val = 0

    for element in vector:
        val += element**2

    return math.sqrt(val)


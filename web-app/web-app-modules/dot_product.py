def dot_product(vec):
    from web_app_tool import final_step
    vector_1, vector_2 = final_step(vec)
    dot_product = 0
    for index in range(len(vector_1)):
        try:
            dot_product += vector_1[index] * vector_2[index]
        except IndexError:
            ""

    return dot_product




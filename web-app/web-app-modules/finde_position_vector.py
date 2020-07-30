def finde_position_vector(vec):
    from web_app_tool import final_step
    point_1, point_2 = final_step(vec)

    for element in range(len(point_1)):
        point_2[element] = point_2[element] - point_1[element]

    return point_2
